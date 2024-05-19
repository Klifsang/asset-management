from flask import request, session
from models.requests import Requests
from models.databaseconfig import db
from models.Notifications import Notifications
def add_requests():
    data = request.get_json()
    asset_id = data['assetId']
    user_id = data['userId']
    comment = data['comment']
    quantity = data['quantity']
    new_request = Requests(asset_id=asset_id, user_id=user_id, comment=comment, quantity=quantity)
    db.session.add(new_request)
    db.session.commit()
    return {"message": "Request added successfully"}, 201
def delete_requests(id):
    rquest = Requests.query.filter_by(id=id).first()
    if rquest:
        db.session.delete(rquest)
        db.session.commit()
    return {"message": "Request deleted successfully"}, 201   

def patch_requests():
    data = request.get_json()
    id = data.get('id')
    rquest = Requests.query.filter_by(id=id).first()
    if rquest:
        for key, value in data.items():
            setattr(rquest, key, value)
            status = "pending"
            if value == "approved":
                status = "approved"
            elif value == "rejected":
                status = "rejected"
        notif = Notifications(request_id=id, status=status, asset_id = rquest.asset_id)
        db.session.add(notif)
        db.session.commit()
    return {"message": "Request updated successfully"}, 201

def get_requests():
    requests = Requests.query.all()
    if requests:
        return [
            {
                "id": request.id,
                "asset_id": request.asset_id,
                "user_id": request.user_id,
                "admin_id": request.admin_id,
                "comment": request.comment,
                "quantity": request.quantity,
                "status": request.status,
                "assigneddate": request.assigneddate,
                "returndate": request.returndate,
                "returnstatus": request.returnstatus,
            }
            for request in requests
        ]
def my_requests():
    id = session["user_id"]
    requests = Requests.query.filter_by(user_id=id).all()
    if requests:
        return [
            {
                "id": request.id,
                "asset_id": request.asset_id,
                "user_id": request.user_id,
                "admin_id": request.admin_id,
                "comment": request.comment,
                "quantity": request.quantity,
                "status": request.status,
                "assigneddate": request.assigneddate,
                "returndate": request.returndate,
                "returnstatus": request.returnstatus,
            }
            for request in requests
        ]
