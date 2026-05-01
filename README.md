## Django Chatbot Web App
A responsive Django-based chatbot application featuring a clean Bootstrap UI. This project supports session-based chat history, dynamic message rendering, and a hybrid backend that uses simple rule-based logic with an optional Machine Learning prediction function.
------------------------------
## 🚀 Features

* Real-time Messaging: Smooth user-to-bot communication interface.
* Session-based History: Maintains chat continuity during the user session.
* Hybrid Logic: Supports both rule-based replies and ML-driven predictions.
* Responsive Design: Fully optimized for mobile and desktop using Bootstrap.
* Chat Management: Functionality to reset chat history easily.
* Dynamic UI: Asynchronous message rendering for a modern feel.

------------------------------
## 🛠️ Tech Stack

* Backend: Django (Python)
* Frontend: HTML5, CSS3, Bootstrap 5
* Data Processing: Jupyter Notebook (for ML model development)
* Database: SQLite (Default)

------------------------------
## 📂 Project Structure

    ├── core/               # Main Django application logic
    ├── Data/               # Datasets for rule-based or ML training
    ├── Model/              # Saved ML models and prediction scripts
    ├── New/                # Additional assets or components
    ├── manage.py           # Django management script
    ├── index.ipynb         # Notebook for model exploration/testing
    └── db.sqlite3          # Local database

------------------------------
## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
  git clone https://github.com/abhaysingh-coder/Django-Chatbot-Web-App
  cd Django-Chatbot-Web-App

### 2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install django, pandas, numpy

### 4️⃣ Apply migrations
python manage.py migrate

### 5️⃣ Run the server
python manage.py runserver

---

## 🎯 Learning Outcomes

+ Understanding Django project structure: Learn how to organize applications, settings, and assets within a professional framework.
+ Implementing CRUD operations: Gain experience in creating, reading, updating, and deleting chat messages and session data.
+ Working with Django ORM and SQLite: Master database interactions using Python objects to store and retrieve chat history.
+ Connecting frontend templates with backend logic: Learn to bridge Django’s Python backend with HTML/CSS to create a dynamic user experience.
+ Using Bootstrap for responsive UI: Build a modern, mobile-friendly chat interface that looks great on any device.

---

## 📌 Future Improvements

+ Integration of LLMs: Implement advanced APIs, such as OpenAI (GPT) or Google Gemini, to replace simple rule-based logic for more natural conversations.
+ User Authentication: Implement a Login/Sign-up system to allow users to save chat history across different devices.
+ WebSockets (Django Channels): Transition from standard HTTP requests to WebSockets for real-time messaging.
+ Voice Recognition: Add Speech-to-Text and Text-to-Speech capabilities to allow users to interact with the bot using voice.
+ Enhanced NLP: Improve the local ML model to better handle intent recognition and complex multi-turn dialogues.
+ Dashboard Analytics: Create an admin panel to visualize chat statistics, common user queries, and bot performance metrics.

---

## 🧠 Usage

* Rule-based Chat: The bot looks for specific keywords in the Data/ folder to provide instant answers.
* ML Integration: For complex queries, the app can be configured to use the model stored in the Model/ directory to predict the best response.

---

## 👨‍💻 Author

Abhay Singh

---

