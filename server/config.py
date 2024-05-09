from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig:
    SECRET_KEY = 'dfsadfdtddasxfta'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./app.sqlite"

    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True