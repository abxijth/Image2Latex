import os 
from dotenv import load_dotenv 
from PIL import Image
from pix2tex.cli import LatexOCR
import io 
import base64
import zmq 
import redis as sredis
import redis.exceptions
load_dotenv()


NUM_WORKERS = int(os.getenv("NUM_WORKERS"))#type:ignore
INFO = bool(os.getenv("INFO"))
ZMQ_WORKER_ADDRESS = "tcp://127.0.0.1:5555"

def worker():
    context = zmq.Context()
    
    socket = context.socket(zmq.PULL)
    socket.bind(ZMQ_WORKER_ADDRESS)
    model = LatexOCR()
    
    if INFO:
        print("[INFO] Worker started!")
    try:
        redis_con = sredis.Redis(decode_responses=True)
        
        redis_con.ping()
    except redis.exceptions.ConnectionError:
        print("[ERROR] Cant Connect to Redis server!")
        return

    while True:
        try:
            
            task :dict = socket.recv_json()#type:ignore
            img_uid = task["id"]
            if INFO:
                print(f"[INFO] Client Image {img_uid} procesing!")
                
            img_b64_string = task["data"]
            try:
                img_bytes = base64.b64decode(img_b64_string)
                img_stream = io.BytesIO(img_bytes)
                img = Image.open(img_stream)
                result = model(img)
                img_stream.close()
                
                redis_con.set(img_uid,f"Result:{str(result)}")
                if INFO:
                    print(f"[INFO] Client Image {img_uid} procesing finished!: {result}")
            except Exception as ex:
                redis_con.set(img_uid,f"Error:{ex}")
            
        except zmq.ZMQError as e:
            print("[ERROR] Worker: ZMQ Error",e)
            break         
        except Exception as e:
            print("[ERROR] Unexpected Error while processing image: ",e)
        
    socket.close()
    context.term()
    redis_con.close()
    print("[INFO] Worker shutting down.")
  