import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../db/dev_item_catelog.db')

DEBUG = True
PORT = 5000
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
