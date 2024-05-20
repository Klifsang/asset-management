import datetime
from server.app import bcrypt, app

with app.app_context():
    from models.admin import Admin
    from models.assets import Assets
    from models.employee import Employee
    from models.requests import Requests
    from models.databaseconfig import db

    asset1 = Assets(
        assetname="car",
        description="Double-cabin",
        condition="brand new",
        availability="available"
        )
    asset2 = Assets(
        assetname="Tipper", 
        description="20 tonnes", 
        condition="brand new", 
        availability="available"
        )

    admin1 = Admin(
        email='wiclifsang@gmail.com', 
        password=bcrypt.generate_password_hash('password').decode('utf-8'), authcode=bcrypt.generate_password_hash('5100').decode('utf-8'), 
        username='klifsang', 
        phonenumber='0123456789', 
        address='112,bomet', 
        role='procurement', 
        level='admin'
        )
    admin2 = Admin(
        email='abel@gmail.com', 
        password=bcrypt.generate_password_hash('password123').decode('utf-8'), authcode =bcrypt.generate_password_hash('5145').decode('utf-8'), 
        username='Abel', 
        phonenumber='0987654321', 
        address='112,Kapsabet', 
        role='CEO', level='admin'
        )
    
    employee1 = Employee(
        username='kelvin', 
        department='Logistics', 
        address='1-Nairobi', 
        email='kelvin@gmail.com', 
        phonenumber='0987654321', 
        password=bcrypt.generate_password_hash('123password').decode('utf-8'), role="cleaning", 
        level='employee'
        )
    employee2 = Employee(
        username='Glen', 
        department='Mechanical', 
        address='100-Nairobi', 
        email='glen@gmail.com', 
        phonenumber='0123456789', 
        password=bcrypt.generate_password_hash('password123').decode('utf-8'), role="typist", 
        level='employee'
        )

    req = Requests(
        asset_id=1,
        user_id=1,
        admin_id=1,
        comment="I need this asset",
        quantity= 1,
        status="pending",
        assigneddate=datetime.date(2021, 4, 1),
        returndate=datetime.date(2021, 4, 2),
        returnstatus="pending"
    )
    req2 = Requests(
        asset_id=2,
        user_id=2,
        admin_id=1,
        comment="I need this asset",
        quantity= 2,
        status="pending",
        assigneddate=datetime.date(2021, 4, 1),
        returndate=datetime.date(2021, 4, 2),
        returnstatus="pending"
    )
    
    db.session.add_all([asset1, asset2, admin1, admin2, employee1, employee2, req, req2])
    db.session.commit()

'''
    # Create a new admin
    # url = /admin/register
    {
        "email" : "weldon@gmail.com",
        "password" : "weldon123", 
        "authcode" : "5100",
        "usernames" : "weldon",
        "phonenumber" : "0713131212",
        "address" : "200-BOMET",
        "role" : "Finance Manager",
        "level" : "admin"
    }

    # Create a new employee
    # url = /staff/register
    {
        "username" : "Tera",
        "department" : "Phlebotomics",
        "address" : "3-SILIBWET",
        "email" : "tera@phlebotomics.com",
        "phonenumber" : "0728888881",
        "password" : "5100",
        "role" : "employee"
    }
    
    # Create request
    # url = /requests/add
    {
        "asset_id" : "1",
        "user_id" : "1",
        "admin_id" : "1",
        "comment" : "ASAP"
    }
'''