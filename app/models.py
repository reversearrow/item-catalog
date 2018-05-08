from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime
import uuid

db = SQLAlchemy()


class Categories(db.Model):
    __tablename__ = 'categories'
    uuid = db.Column(db.String(20), primary_key=True,
                     default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           onupdate=func.now())
    items = db.relationship('Items', backref='category', lazy=True)


class Items(db.Model):
    __tablename__ = 'items'
    uuid = db.Column(db.String(20), primary_key=True,
                     default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           onupdate=func.now())
    category_id = db.Column(db.String, db.ForeignKey(
        'categories.uuid'), nullable=False)
