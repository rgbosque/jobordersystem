import os, secrets

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    COMPANY_NAME = "RHODECO RUBBER PROCESSING SERVICES, INC."