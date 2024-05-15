# app.py
from flask import Flask, jsonify, send_from_directory, session
from functools import wraps
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from config import ApplicationConfig
from models.databaseconfig import db
from flask_bcrypt import Bcrypt
from endpoints.employee_api import delete_employee, patch_employee, register_employee, get_employees
from endpoints.admin_api import delete_admin, patch_admin, register_admin, get_admins
from endpoints.assets_api import add_assets, delete_assets, patch_assets, get_assets
from endpoints.requests_api import add_requests, patch_requests, delete_requests, get_requests
from endpoints.auth_api import get_current_user, login, logout
import os

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/dist',
    template_folder='../client/dist'
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
app.add_url_rule('/user/register', 'register_employee', register_employee, methods=['POST'])
app.add_url_rule('/user/delete', 'delete_employee', delete_employee, methods=['DELETE'])
app.add_url_rule('/user/update', 'patch_employee', patch_employee, methods=['PATCH'])
app.add_url_rule('/user/get', 'get_employees', get_employees, methods=['GET'])

    # admin
app.add_url_rule('/admin/register', 'register_admin', register_admin, methods=['POST'])
app.add_url_rule('/admin/delete', 'delete_admin', delete_admin, methods=['DELETE'])
app.add_url_rule('/admin/update', 'patch_admin', patch_admin, methods=['PATCH'])
app.add_url_rule('/admin/get', 'get_admins', get_admins, methods=['GET'])

    # assets
app.add_url_rule('/assets/add', 'add_assets', add_assets, methods=['POST'])
app.add_url_rule('/assets/delete', 'delete_assets', delete_assets, methods=['DELETE'])
app.add_url_rule('/assets/update', 'patch_assets', patch_assets, methods=['PATCH'])
app.add_url_rule('/assets/get', 'get_assets', get_assets, methods=['GET'])

    # requests
app.add_url_rule('/requests/add', 'add_requests', add_requests, methods=['POST'])
app.add_url_rule('/requests/delete', 'delete_requests', delete_requests, methods=['DELETE'])
app.add_url_rule('/requests/update', 'patch_requests', patch_requests, methods=['PATCH'])
app.add_url_rule('/requests/get', 'get_requests', get_requests, methods=['GET'])

    # Authentication
app.add_url_rule('/checksession', 'checksession', get_current_user, methods=['POST'])
app.add_url_rule('/user/login', 'login', login, methods=['POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['POST'])
app.add_url_rule('/logout', 'logout', logout, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)
