from flask import request
from ..models.requests import Requests
from ..models.databaseconfig import db
def requests():
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
    
    # asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    # admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    # comment = db.Column(db.String)
    # status = db.Column(db.String)
    # assigneddate = db.Column(db.Date)
    # returndate = db.Column(db.Date)
    # returnstatus = db.Column(db.String)