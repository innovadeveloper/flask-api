from sqlalchemy import Integer, String
from sqlalchemy_utils import EmailType
from app.serializers.serializer import Serializer

from app import db


class User(db.Model, Serializer):
    """
    This is a base user Model
    """
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    fullname = db.Column(String(100), nullable=False)
    username = db.Column(String(20), nullable=False, unique=True)
    password = db.Column(String(50), nullable=False)
    email = db.Column(EmailType(), nullable=False, unique=True)
    age = db.Column(Integer)

    def __init__(self, fullname, username, password, email, age = None):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.age = age

    # def serialize(self):
    #     d = Serializer.serialize(self)
    #     del d['password']
    #     return d
