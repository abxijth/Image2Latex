import redis as sredis 
import redis.exceptions 
from worker import worker 
from multiprocessing import Process
from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from RequestsHandle import routes_bp

load_dotenv()

INFO = bool(os.getenv("INFO"))
NUM_WORKERS = int(os.getenv("NUM_WORKERS", 1)) 

print("Flask application starting up...")

try:

    redis_con = sredis.Redis(decode_responses=True)
    redis_con.ping()
    if INFO:
        print("[INFO] Connected to Redis at localhost:6379")
        
except redis.exceptions.ConnectionError:
    print("[ERROR] Cannot connect to Redis server at localhost:6379!")
    exit(1)

app = Flask(__name__)


app.config['REDIS_CONNECTION'] = redis_con
app.config['INFO'] = INFO

####################### CORS CONFIG
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "null",
    "http://127.0.0.1:5000",
    "http://172.24.160.1:5000",
    "http://172.24.160.1:5500",
    "http://localhost:8000"
]
CORS(app, resources={r"/*": {"origins": origins}}, supports_credentials=True)


app.register_blueprint(routes_bp, prefix="/images")

@app.route("/")
def root():
    """
    Root Endpoint
    """
    if app.config['INFO']:
        print("[INFO] root initiated!")
    return jsonify({
        "message": "Image2Latex server is running. POST images to /images/uploadfile/"
    })
    
    
if __name__=="__main__":

    print(f"[INFO] Starting {NUM_WORKERS} worker processes...")
    worker_processes = [Process(target=worker, daemon=True) for _ in range(NUM_WORKERS)]
    
    try:
        for p in worker_processes:
            p.start()
        print(f"[INFO] {NUM_WORKERS} worker processes started.")
        
        # gunicorn -w 4 -b 0.0.0.0:8000 flask_main:app
        app.run(
            host="0.0.0.0",
            port=8000,
            debug=False  
        )
        
    except KeyboardInterrupt:
        print("\n\nShutting Down from Keyboard Interrupt...")
    finally:
        print("Terminating worker processes...")
        for p in worker_processes:
            if p.is_alive():
                p.terminate()
                p.join(timeout=1)
        print("Worker processes terminated.")
        
        print("Closing Redis connection...")
        app.config['REDIS_CONNECTION'].close()
        
        print("Flask server shut down.")

