# 🧮 Image2LaTeX (Backend)  

A simple Flask web app that converts mathematical equation images into LaTeX code using the Pix2Text model.

## 🚀 Features

- Provide an image containing a math equation
- Convert it to LaTeX Code instantly

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

## 🤝 Contributing

1. Fork this repository and clone your forked repository

2. Create a new branch
   
   ```
   git checkout -b feature/new
   ```
   
4. Make your changes
   
5. Commit and push

   ```
   git add .  
   git commit -m "feat: improved backend"  
   git push origin feature/new
   ```
   
6. Open a Pull Request to the main repository on GitHub 🚀

- If you find bugs or have ideas for improvements, open a New Issue in the Issues tab and describe your suggestion or problem clearly.  

## 🧠 Future Improvements

- Better error handling for non-math images
