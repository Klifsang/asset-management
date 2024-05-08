from functools import wraps
from flask import Flask, jsonify, make_response, redirect, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

migrate = Migrate(app, db)

db.init_app(app)

from models import admin, assets, requests, employee
username = 'Klif'
app.secret_key = 'abc123@assets#manager.com'
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # username = request.cookies.get('username')
        if username != 'Kliff':
            # return jsonify({'message': 'This is a protected page'})
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return jsonify({'username': 'admin', 'password': 'password'})

def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        pass
    return jsonify({'message': 'please login'})

app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])

@app.route('/logout')
def logout():
    resp = make_response(jsonify({'message': 'Logout successful'}), 200)
    resp.set_cookie('username', '', expires=0)  # Remove the cookie
    return resp



if __name__ == '__main__':
    app.run(debug=True)

