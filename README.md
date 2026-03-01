# 🎓 Flask Student Management System

A multi-step Student Management System built using **Flask**, **SQLite**, and **SQLAlchemy**.

This project allows users to:
- Register
- Login
- Enter student details (multi-step form)
- Store all data in database after final submission

## 🚀 Features

- 🔐 User Authentication (Register/Login)
- 📝 Multi-Step Form (Basic → Parent → College → Hobbies)
- 💾 Session-based temporary storage
- 🗄 SQLite Database Integration
- 🔒 Password hashing for security


## 🏗 Project Architecture

This project follows a simple **MVC (Model-View-Controller)** architecture pattern.

### 🔹 1. Model (Database Layer)

Defined using SQLAlchemy inside `app.py`.

Models:
- User
- BasicDetails
- ParentDetails
- CollegeDetails
- Hobbies

These models represent database tables.


### 🔹 2. View (Frontend Layer)

HTML files inside:
templates/


CSS file inside:
static/style.css


Handles UI design and form input.

---

### 🔹 3. Controller (Application Logic)

Defined inside:
app.py

Handles:
- Routing
- Form processing
- Session management
- Database operations

---

## 🧠 System Flow (Architecture Diagram)

```
User (Browser)
      │
      ▼
HTML Forms (Templates)
      │
      ▼
Flask Routes (app.py)
      │
      ├── Session Storage (Temporary Data)
      │
      ▼
SQLAlchemy Models
      │
      ▼
SQLite Database (student.db)
```

---

## 🔄 Application Workflow

1. User registers
2. User logs in
3. User fills Basic Details
4. Data stored in session
5. User fills Parent Details
6. User fills College Details
7. User fills Hobbies
8. On final submit → All data stored in database

---

## 🛠 Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3

---

## 📂 Project Structure

```
Flask_Student-Management-system/
│
├── app.py
├── student.db
├── README.md
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── basic.html
│   ├── parent.html
│   ├── college.html
│   └── hobbies.html
│
└── static/
    └── style.css
```

---

## ⚙️ How to Run This Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Yasaswiniravi/Flask_Student-Management-system.git
cd Flask_Student-Management-system
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask flask_sqlalchemy
```

### 4️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🔐 Security Features

- Password hashing using Werkzeug
- Session-based authentication
- Protected routes
