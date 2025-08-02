# Attendly

**Attendly** is a Django-based Student Attendance Management System designed to help schools and colleges manage students, teachers, classrooms, and attendance records efficiently.

## 🚀 Features

- 📋 Add, edit, delete, and list students  
- 👨‍🏫 Manage teachers and their classes  
- 🏫 Assign classrooms to teachers  
- ✅ Mark and track student attendance  
- 🔐 Admin panel support for managing records  
- 🧩 Modular codebase following Django best practices  

## 🛠️ Tech Stack

- **Backend**: Python, Django  
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)  
- **Frontend**: HTML, CSS (via Django templates)  

## 📁 Project Structure
attendly/
---- core/       # Project Settings
---- stattsys/   # Main app (Students, Teachers, Attendance logic)
---- templates/  # HTML templates for UI
---- manage.py   # Django management script
---- db.sqlite3  # Default development databse

## ⚙️ Setup Instructions (for local development)

1. **Clone the repository**

```bash
    git clone https://github.com/YOUR_USERNAME/attendly.git
    cd attendly

2. **Create and Activate Virtual environment**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
    pip install -r requirements.txt

4. **Apply migrations and start the server**
    python manage.py migrate
    python manage.py runserver

5. **Visit the app**
    Open http://127.0.0.1:8000 in your browser.


## 🧪 Development Status

    🔨 This project is currently under active development. CRUD operations for all models are being implemented step by step.

## 📜 License

This project is open-source under the MIT License. Feel free to use and adapt it.

## 🙌 Acknowledgments

Built with ❤️ using Django.

## ✨ Future Improvements

- User login/authentication  
- Attendance reports  
- CSV export/import  
- Role-based access control  


