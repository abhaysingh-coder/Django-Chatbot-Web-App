# 🤖 Django Chatbot Web App

A responsive Django-based chatbot web application with a clean Bootstrap UI, session-based chat history, user-bot messaging, chat reset functionality, and optional machine-learning-based prediction support.
------------------------------

## 🚀 Features

- User-friendly chatbot interface
- Session-based chat History: Maintains chat continuity during the user session.
- User and bot message rendering
- Reset chat option
- Responsive Design: Fully optimized for mobile and desktop using Bootstrap.
- Django backend integration
- Optional ML model prediction support
- SQLite database support
- Jupyter Notebook included for model experimentation
------------------------------

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | SQLite |
| ML / Data | Pandas, NumPy, Pickle, Jupyter Notebook |
| UI Icons | Font Awesome |
------------------------------

## 📂 Project Structure

    Django-Chatbot-Web-App/
    │
    ├── core/                            # Main Django application logic
    │   ├── static/
    │   ├── templates/
    │   ├── migrations/
    │   ├── chatbot.py
    │   ├── models.py
    │   ├── views.py
    │   ├── admin.py
    │   └── apps.py
    │
    ├── Data/                          # Datasets for rule-based or ML training
    │   └── Dataset files
    │
    ├── Model/                         # Saved ML models and prediction scripts
    │   └── Saved ML model files
    │
    ├── New/                           # Additional assets or components
    │
    ├── manage.py                      # Django management script
    ├── index.ipynb                    # Notebook for model exploration/testing
    └── db.sqlite3                     # Local database
    └── README.md
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
------------------------------

## 🎯 Learning Outcomes
By building this project, the following concepts and skills were developed:

- Understanding of Django framework architecture (MVT pattern)
- Handling HTTP requests and responses in Django
- Session management for maintaining chat history
- Designing responsive UI using Bootstrap
- Integration of frontend and backend components
- Working with SQLite database in Django
- Implementation of chatbot logic (rule-based / ML-based)
- Loading and using trained models with Pickle
- Data preprocessing using Pandas and NumPy
- Debugging and optimizing Django applications
- Basic understanding of machine learning pipeline for NLP tasks
- Structuring a full-stack web application project

This project strengthens both backend development and foundational AI integration concepts.
------------------------------

## 📌 Future Improvements

The current system provides a basic chatbot web application, but it can be enhanced further with the following improvements:

- Implement user authentication (login/signup system)
- Store chat history permanently in the database instead of sessions
- Improve chatbot intelligence using advanced NLP models (e.g., transformers)
- Integrate external APIs like OpenAI or Dialogflow for smarter responses
- Add voice input and speech-to-text functionality
- Implement text-to-speech for bot responses
- Add real-time chat using WebSockets (Django Channels)
- Create an admin dashboard for monitoring chats and users
- Improve UI/UX with modern frontend frameworks like React
- Deploy the application on cloud platforms (Render, AWS, or Heroku)
- Add multilingual support for wider accessibility
- Optimize model performance and increase accuracy
- Add logging and analytics for chatbot interactions
- Implement REST API for mobile or third-party integration
------------------------------

## 🧠 Usage

Follow these steps to use the chatbot application:

1. Start the Django development server:
   ```bash
   python manage.py runserver
   
2. Open your browser and go to:
   ```bash
    http://127.0.0.1:8000/

4. (Optional) Login using default credentials (if implemented):
   ```bash
   Username: admin
   Password: Abhay12345@

6. Type your message in the chatbot input box.
7. Press Send or hit Enter to submit your message.
8. The chatbot will process your input and display a response.
9. Continue the conversation as needed.
10. Click on Reset Chat to clear the current session and start a new conversation.
------------------------------

## 👨‍💻 Author

Abhay Singh
