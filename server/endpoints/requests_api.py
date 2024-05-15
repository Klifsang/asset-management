from flask import request
from models.requests import Requests
from models.databaseconfig import db
def add_requests():
    data = request.get_json()
    asset_id = data['asset_id']
    user_id = data['user_id']
    admin_id = data['admin_id']
    comment = data['comment']
    status = data['status']
    assigneddate = data['assigneddate']
    returndate = data['returndate']
    returnstatus = data['returnstatus']
    
    request = Requests(asset_id=asset_id, user_id=user_id, admin_id=admin_id, comment=comment, status=status, assigneddate=assigneddate, returndate=returndate, returnstatus=returnstatus)
    db.session.add(request)
    db.session.commit()
    return {"message": "Request added successfully"}, 201
def delete_requests():
    data = request.get_json()
    id = data.get('id')
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
                "status": request.status,
                "assigneddate": request.assigneddate,
                "returndate": request.returndate,
                "returnstatus": request.returnstatus,
            }
            for request in requests
        ]
    # asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    # admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # comment = db.Column(db.String)
    # status = db.Column(db.String)
    # assigneddate = db.Column(db.Date)
    # returndate = db.Column(db.Date)
    # returnstatus = db.Column(db.String)