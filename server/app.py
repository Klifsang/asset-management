# app.py
from flask import Flask, jsonify, send_from_directory, session
from functools import wraps
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from config import ApplicationConfig
from models.databaseconfig import db
from flask_bcrypt import Bcrypt
from endpoints.employee_api import delete_employee, patch_employee, register_employee, get_employees,getstaff
from endpoints.admin_api import delete_admin, patch_admin, register_admin, get_admins
from endpoints.assets_api import add_assets, delete_assets, patch_assets, get_assets
from endpoints.requests_api import add_requests, patch_requests, delete_requests, get_requests, my_requests
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

from models import admin, assets, requests, employee, Notifications

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id")
        if user_id is None:
            return jsonify({'message': 'This is a protected page'}), 401
        return f(*args, **kwargs)
    return decorated_function

def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_level = session.get("user_level")
        if user_level != 'admin':
            return jsonify({'message': 'This is allowed for admins only'}), 401
        return f(*args, **kwargs)
    return decorated_function



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and path.startswith('api'):
        return "API route", 404
    return send_from_directory(app.static_folder, 'index.html')







# endpoints
    # employees
app.add_url_rule('/api/staff/register', 'register_employee', register_employee, methods=['POST'])
app.add_url_rule('/api/staff/delete', 'delete_employee', is_admin(delete_employee), methods=['DELETE'])
app.add_url_rule('/api/staff/update', 'patch_employee', login_required(patch_employee), methods=['PATCH'])
app.add_url_rule('/api/staff/get', 'get_employees', login_required(get_employees), methods=['GET'])
app.add_url_rule('/api/staff/getstaff', 'getstaff', login_required(getstaff), methods=['POST'])
    # admin
app.add_url_rule('/api/admin/register', 'register_admin', register_admin, methods=['POST'])
app.add_url_rule('/api/admin/delete', 'delete_admin', is_admin(delete_admin), methods=['DELETE'])
app.add_url_rule('/api/admin/update', 'patch_admin', patch_admin, methods=['PATCH'])
app.add_url_rule('/api/admin/get', 'get_admins', get_admins, methods=['GET'])

    # assets
app.add_url_rule('/api/assets/add', 'add_assets', is_admin(add_assets), methods=['POST'])
app.add_url_rule('/api/assets/delete', 'delete_assets', is_admin(delete_assets), methods=['DELETE'])
app.add_url_rule('/api/assets/update', 'patch_assets', patch_assets, methods=['PATCH'])
app.add_url_rule('/api/assets/get', 'get_assets', login_required(get_assets), methods=['GET'])

    # requests
app.add_url_rule('/api/requests/add', 'add_requests', login_required(add_requests), methods=['POST'])
app.add_url_rule('/api/requests/delete/<int:id>', 'delete_requests', login_required(delete_requests), methods=['DELETE'])
app.add_url_rule('/api/requests/update', 'patch_requests', is_admin(patch_requests), methods=['PATCH'])
app.add_url_rule('/api/requests/get', 'get_requests', login_required(get_requests), methods=['GET'])
app.add_url_rule('/api/myrequests/get', 'my_requests', login_required(my_requests), methods=['GET'])


    # Authentication
app.add_url_rule('/api/checksession', 'checksession', get_current_user, methods=['POST'])
app.add_url_rule('/api/user/login', 'login', login, methods=['POST'])
app.add_url_rule('/api/logout', 'logout', logout, methods=['POST'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
