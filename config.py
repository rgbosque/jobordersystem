import os, secrets

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    COMPANY_NAME = "RHODECO RUBBER PROCESSING SERVICES, INC."
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'jo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False