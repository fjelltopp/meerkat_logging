"""
config.py

Configuration and settings
"""
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI",
                                        'postgresql+psycopg2://postgres:postgres@localhost/event_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_URL = os.getenv("LOGGING_URL", "http://nginx/logging")
    LOGGING_SOURCE = os.getenv("DEPLOYMENT",
                                'test')
    LOGGING_SOURCE_TYPE = "logger"
    LOGGING_IMPLEMENTATION = "meerkat"
    
class Production(Config):
    DEBUG = False
    TESTING = False

    
class Development(Config):
    DEBUG = True
    TESTING = False


class Testing(Config):
    DEBUG = False
    TESTING = True
