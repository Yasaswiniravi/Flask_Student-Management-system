# Flask Student Management System – Code Explanation

This document explains the main parts of the `app.py` file in a simple and easy way.
The application is built using **Flask, SQLAlchemy, and SQLite**.
---
# 1. Importing Required Libraries

```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
```

### Purpose

These libraries provide the core functionality for the application.

| Library                | Purpose                        |
| ---------------------- | ------------------------------ |
| Flask                  | Creates the web application    |
| render_template        | Displays HTML pages            |
| request                | Gets form data entered by user |
| redirect               | Moves user to another page     |
| url_for                | Generates URL for routes       |
| session                | Temporarily stores user data   |
| SQLAlchemy             | Connects Flask with database   |
| generate_password_hash | Encrypts password              |
| check_password_hash    | Verifies password during login |

---

# 2. Creating Flask Application

```python
app = Flask(__name__)
```

This line creates the Flask application.

`__name__` tells Flask where the application is located.

---

# 3. Secret Key

```python
app.secret_key = "supersecretkey"
```

The secret key is used to **secure session data**.

Session stores temporary data such as:

* Logged-in user
* Form details between pages

Without a secret key, Flask cannot use sessions.

---

# 4. Database Configuration

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### Explanation

| Configuration                  | Meaning                      |
| ------------------------------ | ---------------------------- |
| SQLALCHEMY_DATABASE_URI        | Location of database         |
| sqlite:///student.db           | Creates SQLite database file |
| SQLALCHEMY_TRACK_MODIFICATIONS | Disables extra memory usage  |

---

# 5. Connecting Flask to Database

```python
db = SQLAlchemy(app)
```

This connects the Flask application with SQLAlchemy so we can create tables and store data.

---

# 6. Database Models (Tables)

Models define the **database structure**.

Each class represents a table.

---

## User Table

```python
class User(db.Model):
```

Stores login information.

| Column   | Purpose            |
| -------- | ------------------ |
| id       | Primary key        |
| email    | User email         |
| password | Encrypted password |

---

## BasicDetails Table

Stores basic student information.

Fields include:

* Name
* Branch
* College Name
* Year Passed
* Email
* Phone
* Address
* Date of Birth

Each record is linked to a **user_id**.

---

## ParentDetails Table

Stores parent information.

Fields include:

* Father Name
* Father Occupation
* Father Phone
* Mother Name
* Mother Phone
* Address

---

## CollegeDetails Table

Stores college-related information.

Fields include:

* College Name
* Student ID
* Branch
* College Address

---

## Hobbies Table

Stores student hobbies.

Field:

* hobbies

---

# 7. Home Route

```python
@app.route('/')
def index():
    return render_template("index.html")
```

### What it does

This is the **home page** of the application.

When user opens:

```
http://127.0.0.1:5000/
```

Flask loads the **index.html** page.

---

# 8. Register Function

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
```

This function handles **user registration**.

### GET Request

Shows the registration form.

### POST Request

When the user submits the form:

1. Email and password are received.
2. Password is encrypted using `generate_password_hash`.
3. Checks if the user already exists.
4. Saves user into database.

Then redirects to login page.

---

# 9. Login Function

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
```

This function handles **user login**.

### Steps

1. User enters email and password.
2. Database checks if the user exists.
3. Password is verified using `check_password_hash`.
4. If correct:

```
session['user_id'] = user.id
```

This means the user is now logged in.

User is redirected to **Basic Details page**.

---

# 10. Basic Details Page

```python
@app.route('/basic', methods=['GET', 'POST'])
def basic():
```

### Purpose

Collects student basic information.

### Important Logic

If user is not logged in:

```
if 'user_id' not in session:
```

User is redirected to login page.

### When form is submitted

```
session['basic'] = request.form.to_dict()
```

Form data is stored temporarily in **session**.

Then the user is moved to the next page.

---

# 11. Parent Details Page

```python
@app.route('/parent', methods=['GET', 'POST'])
def parent():
```

This page collects parent information.

The data is stored in session:

```
session['parent'] = request.form.to_dict()
```

Then the user moves to the next page.

---

# 12. College Details Page

```python
@app.route('/college', methods=['GET', 'POST'])
def college():
```

Collects college information.

The data is stored in session:

```
session['college'] = request.form.to_dict()
```

Then the user moves to the hobbies page.

---

# 13. Final Submit – Hobbies Page

```python
@app.route('/hobbies', methods=['GET', 'POST'])
def hobbies():
```

This is the **final step**.

When user clicks submit:

All data stored in session is retrieved.

```
basic = session.get('basic')
parent = session.get('parent')
college = session.get('college')
hobbies = session.get('hobbies')
```

Then data is stored into database tables:

```
db.session.add(...)
```

Finally:

```
db.session.commit()
```

This saves all data permanently in the database.

---

# 14. Clearing Session Data

After saving data:

```
session.pop('basic')
session.pop('parent')
session.pop('college')
session.pop('hobbies')
```

This removes temporary form data from session.

---

# 15. Running the Application

```python
if __name__ == "__main__":
```

This block runs the application.

### Database Creation

```
db.create_all()
```

Creates all tables automatically if they don't exist.

### Start Server

```
app.run(debug=True)
```

Starts Flask development server.

---

# 16. Application Workflow

1. User opens website
2. Registers account
3. Logs in
4. Enters Basic Details
5. Enters Parent Details
6. Enters College Details
7. Enters Hobbies
8. Clicks Submit
9. Data is stored in database

---

# Conclusion

This project demonstrates:

* Flask web development
* User authentication
* Multi-step forms
* Session management
* Database storage using SQLAlchemy
* Secure password handling
