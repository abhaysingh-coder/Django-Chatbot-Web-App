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

   1. Clone the Repository
   
       git clone https://github.com
       cd Django-Chatbot-Web-App
   
   2. Create a Virtual Environment
   
       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   3. Install Dependencies
       (Ensure you have Django and necessary ML libraries installed)
       
       pip install django pandas numpy  # Add other dependencies as needed
   
   4. Run Migrations
       
       python manage.py migrate
   
   5. Start the Server
   
       python manage.py runserver
   
   6. Access the App
       Open your browser and go to http://127.0.0.

------------------------------
## 🧠 Usage

* Rule-based Chat: The bot looks for specific keywords in the Data/ folder to provide instant answers.
* ML Integration: For complex queries, the app can be configured to use the model stored in the Model/ directory to predict the best response.

------------------------------
## 🤝 Contributing
    Contributions are welcome! Feel free to open an Issue or submit a Pull Request to improve the chatbot's logic or UI.
------------------------------
## 📄 License
    This project is open-source. Please check the repository for specific licensing details.
------------------------------
## Developed by Abhay Singh

