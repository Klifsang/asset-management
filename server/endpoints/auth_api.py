from flask import jsonify, request, session
from models.employee import Employee
from models.admin import Admin

def login():
    print(session.get("user_id"))
    from app import bcrypt
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    user = Employee.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"error": "Unauthorized"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Username or password incorrect"}), 401
    
    session["user_id"] = user.id
    session["user_role"] = "employee"
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
    return jsonify({"message": "Logged out successfully"}), 200