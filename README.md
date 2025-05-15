# Real-Time Facial Expression Recognition Web App

A real-time facial expression recognition web app built with **TensorFlow**, **OpenCV**, and **Flask**. The app uses your webcam to detect faces and predict their emotions using a trained CNN model.

---

## 🚀 Features

* 🎥 Real-time emotion recognition via webcam
* 🧠 Deep learning model (CNN) trained on grayscale facial images (48x48)
* 💻 Flask backend with Bootstrap-powered responsive UI
* 🌙 Dark mode toggle with CSS animations
* ⏳ Loading spinner for smoother UX

---

## 🧰 Tech Stack

* Python 3.x
* TensorFlow / Keras
* OpenCV
* Flask (Jinja templates)
* Bootstrap 5

---

## 🗂️ Project Structure

```
facial-expression-recognition-Web-App/
├── app.py                  # Flask application
├── video_feed.py           # Real-time frame processing
├── facial_expression_model.h5  # Trained CNN model
├── style.css           # Custom styling
├── index.html          # Frontend UI
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
$ git clone https://github.com/Ishan-giri-05293/facial-expression-recognition-Web-App
$ cd facial-expression-recognition-Web-App

# 2. Create a virtual environment (optional but recommended)
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run the app
$ python app.py

# 5. Visit in browser
Open http://127.0.0.1:5000/
```
📸 Demo Screenshot

![Screenshot 2025-05-15 214651](https://github.com/user-attachments/assets/5f0eaa4a-1cea-4956-b230-43a8ca6bc918)


---
