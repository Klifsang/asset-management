from flask import request
from ..models.assets import Asset
from ..models.databaseconfig import db
def assets():
    data = request.get_json()
    assetname = data.get('assetname')
    description = data.get('description')
    condition = data.get('condition')
    availability = data.get('availability')
    
    asset = Asset(assetname=assetname, description=description, condition=condition, availability=availability)
    
    db.session.add(asset)
    db.session.commit()
    # assetname = db.Column(db.String)
    # description = db.Column(db.String)
    # condition = db.Column(db.String)
    # availability = db.Column(db.String)