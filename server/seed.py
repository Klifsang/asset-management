from models import admin, assets, requests, employee
from app import app
from models.databaseconfig import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

with app.app_context():
    # Assets
    # id = db.Column(db.Integer, primary_key=True)
    # assetname = db.Column(db.String)
    # description = db.Column(db.String)
    # condition = db.Column(db.String)
    # availability = db.Column(db.String)
    asset1 = assets.Assets(assetname="car",description="Double-cabin",condition="brand new",availability="availabe")
    asset2 = assets.Assets(assetname="Tipper",description="20 tonnes",condition="brand new",availability="availabe")

    admin1 = admin.Admin(email='wiclifsang@gmail.com', password=bcrypt.generate_password_hash('password'), username='klifsang', phonenumber='0123456789', address='112,bomet', role='procurement')
    admin2 = admin.Admin(email='abel@gmail.com', password=bcrypt.generate_password_hash('password123'), username='Abel', phonenumber='0987654321', address='112,Kapsabet', role='CEO')
    
    employee1 = employee.Employee(username='kelvin@gmail.com', department='Logistics', address='1-Nairobi',email='kelvin@gmail.com',phonenumber='0987654321',password=bcrypt.generate_password_hash('123password'))
    employee2 = employee.Employee(username='Glen@gmail.com', department='Mechanical', address='100-Nairobi',email='glen@gmail.com',phonenumber='0123456789',password=bcrypt.generate_password_hash('password123'))
    
    db.session.add_all([asset1,asset2,admin1, admin2, employee1, employee2])
    db.session.commit()
    
    # hashed_password = bcrypt.generate_password_hash(password)