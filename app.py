from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='/static')


app = Flask(__name__)
app.secret_key = 'abcdgoutam@session'  # Set a secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Ensure that database creation happens within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    name = session.get('name')
    logged_in = True if name else False
    return render_template('index.html', logged_in=logged_in, name=name)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['name'] = user.name
            return redirect(url_for('index'))
        else:
            return "Invalid email or password"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter_by(name=name).first()
        if existing_user:
            return "Username already exists"
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
