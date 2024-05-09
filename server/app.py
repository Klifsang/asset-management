# app.py
from flask import Flask, jsonify, make_response, redirect, request, session, url_for
from functools import wraps
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from config import ApplicationConfig
from models.databaseconfig import db
import os

app = Flask(__name__)
app.config.from_object(ApplicationConfig)

CORS(app, supports_credentials=True)
# db = SQLAlchemy()
migrate = Migrate(app, db)
server_session = Session(app)
db.init_app(app)

from models import admin, assets, requests, employee
user_name = 'Klif'
pass_word = '5100'

app.secret_key = os.urandom(24)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # username = session['username']
        # print(username)
        if 'username' not in session:
            return jsonify({'message': 'This is a protected page'})
            # return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return jsonify({'username': 'admin', 'password': 'password'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email != user_name or password != pass_word:
        return jsonify({'message': 'Invalid credentials'}), 401

    resp = make_response(jsonify({'message': 'Login successful'}), 200)
    session['email'] = email  # Store email in session
    print(session)
    return resp

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email != user_name or password != pass_word:
        return jsonify({'message': 'Invalid credentials'}), 401

    # Set a cookie to mark the user as authenticated
    resp = make_response(jsonify({'message': 'Login successful'}), 200)
    session['email'] = email  # Store email in session
    print(session)
    return resp

@app.route('/logout')
def logout():
    resp = make_response(jsonify({'message': 'Logout successful'}), 200)
    session.pop('email', None)  # Remove username from session
    return resp

if __name__ == '__main__':
    app.run(debug=True)
