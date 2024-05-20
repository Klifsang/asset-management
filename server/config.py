from datetime import timedelta
from dotenv import load_dotenv
from server.models.databaseconfig import db
load_dotenv()

class ApplicationConfig:
    SECRET_KEY = 'dfsadfdtddasxfta'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./app.sqlite"

    SESSION_TYPE = "sqlalchemy"
    SESSION_SQLALCHEMY = db
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_USE_SIGNER = True