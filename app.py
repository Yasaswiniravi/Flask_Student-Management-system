from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------- MODELS --------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))

class BasicDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    college_name = db.Column(db.String(200))
    year_passed = db.Column(db.String(20))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(300))
    dob = db.Column(db.String(20))

class ParentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    father_name = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    father_phone = db.Column(db.String(20))
    mother_name = db.Column(db.String(100))
    mother_phone = db.Column(db.String(20))
    address = db.Column(db.String(300))

class CollegeDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    college_name = db.Column(db.String(200))
    student_id = db.Column(db.String(50))
    branch = db.Column(db.String(100))
    college_address = db.Column(db.String(300))

class Hobbies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    hobbies = db.Column(db.String(500))


# -------------------- HOME --------------------

@app.route('/')
def index():
    return render_template("index.html")


# -------------------- REGISTER --------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(email=email).first():
            return "User already exists!"

        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("register.html")


# -------------------- LOGIN --------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session.clear()   # clear first
            session['user_id'] = user.id
            return redirect(url_for('basic'))

        return "Invalid Credentials"

    return render_template("login.html")


# -------------------- BASIC DETAILS --------------------

@app.route('/basic', methods=['GET', 'POST'])
def basic():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        session['basic'] = request.form.to_dict()
        return redirect(url_for('parent'))

    data = session.get('basic', {})
    return render_template("basic.html", data=data)


# -------------------- PARENT DETAILS --------------------

@app.route('/parent', methods=['GET', 'POST'])
def parent():
    if request.method == 'POST':
        session['parent'] = request.form.to_dict()
        return redirect(url_for('college'))

    data = session.get('parent', {})
    return render_template("parent.html", data=data)


# -------------------- COLLEGE DETAILS --------------------

@app.route('/college', methods=['GET', 'POST'])
def college():
    if request.method == 'POST':
        session['college'] = request.form.to_dict()
        return redirect(url_for('hobbies'))

    data = session.get('college', {})
    return render_template("college.html", data=data)


# -------------------- FINAL SUBMIT (HOBBIES) --------------------

@app.route('/hobbies', methods=['GET', 'POST'])
def hobbies():
    if request.method == 'POST':

        session['hobbies'] = request.form.to_dict()

        # 🔥 Now store ALL data into DB

        user_id = session['user_id']

        basic = session.get('basic')
        parent = session.get('parent')
        college = session.get('college')
        hobbies = session.get('hobbies')

        db.session.add(BasicDetails(user_id=user_id, **basic))
        db.session.add(ParentDetails(user_id=user_id, **parent))
        db.session.add(CollegeDetails(user_id=user_id, **college))
        db.session.add(Hobbies(user_id=user_id, **hobbies))

        db.session.commit()

        # Clear temporary data
        session.pop('basic', None)
        session.pop('parent', None)
        session.pop('college', None)
        session.pop('hobbies', None)

        return "Data Stored Successfully!"

    data = session.get('hobbies', {})
    return render_template("hobbies.html", data=data)


# -------------------- RUN --------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)