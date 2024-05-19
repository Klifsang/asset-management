from flask import request
from models.assets import Assets
from models.databaseconfig import db
def add_assets():
    data = request.get_json()
    assetname = data.get('assetname')
    description = data.get('description')
    condition = data.get('condition')
    availability = data.get('availability')
    quantity = data.get('quantity')
    asset = Assets(assetname=assetname, description=description, condition=condition, availability=availability, quantity=quantity)
    
    db.session.add(asset)
    db.session.commit()
    return {"message": "Asset added successfully"}, 201 
def delete_assets():
    data = request.get_json()
    id = data.get('id')
    asset = Assets.query.filter_by(id=id).first()
    if asset:
        db.session.delete(asset)
        db.session.commit()
    return {"message": "Asset deleted successfully"}, 201   

def patch_assets():
    data = request.get_json()
    id = data.get('id')
    asset = Assets.query.filter_by(id=id).first()
    if asset:
        for key, value in data.items():
            setattr(asset, key, value)
        db.session.commit()
    return {"message": "Asset updated successfully"}, 201

def get_assets():
    assets = Assets.query.all()
    if assets:
        return [
            {
                "id": asset.id,
                "assetname": asset.assetname,
                "description": asset.description,
                "condition": asset.condition,
                "availability": asset.availability,
            }
            for asset in assets
        ]