# 🧮 Image2LaTeX

A simple Flask web app that converts mathematical equation images into LaTeX code using the Pix2Text model.

## 🚀 Features

- Upload an image containing a math equation
- Convert it to LaTeX instantly
- Display the generated LaTeX code in the browser

## 🛠️ Setup Instructions

1. Clone the repository
   
   ```  
   git clone https://github.com/amfoss/Image2Latex.git  
   cd Image2Latex
   ```

3. Create a virtual environment

   ```
   python3 -m venv venv  
   source venv/bin/activate   # on Linux or macOS  
   venv\Scripts\activate      # on Windows
   ```

5. Install dependencies
   ```
   pip install -r requirements.txt
   ```

7. Run the Flask app

   ```
   python3 main.py
   ```

The app will run at: ```http://127.0.0.1:5000```

## 🧑‍💻 Project Structure

Image2Latex/  
├── main.py              # Flask backend  
├── templates/  
│   └── index.html       # Frontend HTML  
├── venv/                # Virtual environment (ignored)  
└── README.md  

## 🤝 Contributing (Example For Frontend)

1. Fork this repository and clone your forked repository

2. Create a new branch
   
   ```
   git checkout -b feature/frontend
   ```
   
4. Make your changes
   
5. Commit and push

   ```
   git add .  
   git commit -m "feat: improve frontend design"  
   git push origin feature/frontend
   ```
   
6. Open a Pull Request to the main repository on GitHub 🚀

## If you find bugs or have ideas for improvements, open a New Issue in the Issues tab and describe your suggestion or problem clearly.  

## 🧠 Future Improvements

- Better error handling for non-math images  
- Improved UI/UX  
- Drag-and-drop uploads  

## 🧑‍🤝‍🧑 Contributors

-
- 
- 
