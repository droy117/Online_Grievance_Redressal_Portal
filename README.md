# Online_Grievance_Redressal_Portal
A simple portal for grievance redressal made using Django


# Local Machine Setup
To run this Django app locally on your machine follow the steps below:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/droy117/Online_Grievance_Redressal_Portal.git
   ```

2. **Navigate to the Repository**:
   ```sh
   cd Online_Grievance_Redressal_Portal
   ```
3. **Create and activate a virtual environment**
   ```sh
   # For Linux
   python3 -m venv venv
   source venv/bin/activate

   # For Windows
   python -m venv venv
   source venv/Scripts/activate
   ```
4. **Run the application**
   ```sh
   pip install django
   python manage.py migrate
   python manage.py runserver
   ```
5. **Open in browser**
   Go to http://127.0.0.1:8000/ or type ```localhost:8000```
