from flask import jsonify, request, session
from server.models.Notifications import Notifications
from server.app import db

def get_notifications():
    """
    Returns a list of all notifications
    """
    id = session["user_id"]
    notifs = Notifications.query.filter_by(user_id = id).all()
    return jsonify(notifs.to_dict()),200

def delete_notifications():
    """
    Deletes all notifications
    """
    id = request.get_json("id")
    Notifications.query.filter_by(user_id = id).delete()
    db.session.commit()
    return jsonify({"message": "Notifications deleted"}),200