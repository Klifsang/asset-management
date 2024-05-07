from models import admin, assets, requests, employee
from app import db, app

with app.app_context():
    # Assets
    # id = db.Column(db.Integer, primary_key=True)
    # assetname = db.Column(db.String)
    # description = db.Column(db.String)
    # condition = db.Column(db.String)
    # availability = db.Column(db.String)
    asset1 = assets.Assets(assetname="car",description="Double-cabin",condition="brand new",availability="availabe")
    asset2 = assets.Assets(assetname="Tipper",description="20 tonnes",condition="brand new",availability="availabe")
    asset3 = assets.Assets(assetname="Lawn mower",description="5000 rpm",condition="brand new",availability="availabe")
    db.session.add(asset1)
    db.session.add(asset2)
    db.session.add(asset3)

    db.session.commit()