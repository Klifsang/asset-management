# app.py
from flask import Flask, jsonify, send_from_directory, session
from functools import wraps
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from config import ApplicationConfig
from models.databaseconfig import db
from flask_bcrypt import Bcrypt
from endpoints.employee_api import delete_employee, patch_employee, register_employee, login_employee,get_current_user,logout_employee
from endpoints.admin_api import delete_admin, patch_admin, register_admin
from endpoints.assets_api import add_assets, delete_assets, patch_assets
import os

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../../client/dist',
    template_folder='../../client/dist'
)
app.config.from_object(ApplicationConfig)

CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

db.init_app(app)
app.secret_key = os.urandom(24)
# Initialize the Flask Session
Session(app)
migrate = Migrate(app, db)
# db.create_all()

from models import admin, assets, requests, employee

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return jsonify({'message': 'This is a protected page'})
        return f(*args, **kwargs)
    return decorated_function

# @app.route("/checksession", methods=["get", "post"])

@app.route('/')
# @login_required
def home():
    return send_from_directory(app.static_folder, 'index.html')

# endpoints
# employees
app.add_url_rule('/user/register', 'register', register_employee, methods=['POST'])
app.add_url_rule('/user/login', 'login', login_employee, methods=['POST'])
app.add_url_rule('/user/delete', 'delete', delete_employee, methods=['POST'])
app.add_url_rule('/user/update', 'update', patch_employee, methods=['POST'])
app.add_url_rule('/logout', 'logout', logout_employee, methods=['POST'])

# admin
app.add_url_rule('/admin/register', 'register', register_admin, methods=['POST'])
app.add_url_rule('/admin/delete', 'delete', delete_admin, methods=['POST'])
app.add_url_rule('/admin/update', 'update', patch_admin, methods=['POST'])


# assets
app.add_url_rule('/assets/add', 'add', add_assets, methods=['POST'])
app.add_url_rule('/assets/delete', 'delete', delete_assets, methods=['POST'])
app.add_url_rule('/assets/add', 'add', add_assets, methods=['POST'])

app.add_url_rule('/checksession', 'checksession', get_current_user, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
