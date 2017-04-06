"""
config.py

Configuration and settings
"""
import os


class Config(object):
    DEBUG = False
    TESTING = False
    USERNAME = "admin"
    PASSWORD = "secret"
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI",
                                        'postgresql+psycopg2://postgres:postgres@localhost/event_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_URL = "http://nginx/logging"
    LOGGING_SOURCE = "test"
    LOGGING_SOUCRE_TYPE = "test"
    LOGGING_IMPLEMENTAION = "null_island"
    
class Production(Config):
    DEBUG = False
    TESTING = False

    
class Development(Config):
    DEBUG = True
    TESTING = False


class Testing(Config):
    DEBUG = False
    TESTING = True
