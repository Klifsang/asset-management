from flask import jsonify, request, session
from server.models.employee import Employee
from server.models.admin import Admin

def login():
    from app import bcrypt
    data = request.get_json()
    print(data)
    username = data.get('username')
    password = data.get('password')
    authcode = data.get('authcode')
    print(username, password, authcode)
    user = None
    is_admin = False
    if authcode:
        user = Admin.query.filter_by(username=username).first()
        is_admin = True if user is not None else False 
    else:
        user = Employee.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"error": "Unauthorized"}), 401
    
    if is_admin and not bcrypt.check_password_hash(user.authcode, authcode):
        return jsonify({"error": "Username or password & authcode do not match"}), 401
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Username or password incorrect"}), 401
    
    session["user_id"] = user.id
    session["user_level"] = "admin" if is_admin else "employee"
    print(session.get("user_id"))
    get_current_user()
    return jsonify({
        "id": user.id,
        "username": user.username,
    }), 200
    


def get_current_user():
    user_id = session.get("user_id")
    print(user_id)
    if user_id is None:
        return jsonify({"error": "Unauthorized"}), 401
    
    # user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user_id,
    }) 
    
def logout():
    session.pop("user_id", None)
    session.pop("user_level", None)
    return jsonify({"message": "Logged out successfully"}), 200