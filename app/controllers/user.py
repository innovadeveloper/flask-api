from flask_restful import Resource
from flask import jsonify
# from app.models.user import User as UserDB
import json
from app.serializers.serializer import Serializer
from app.main.database import db
from app.models.user import User as UserDB
import time

class User(Resource):
    def get(self, id):
        user = UserDB("kenny", "k407" + str(time.time_ns()), "123", "innova" + str(time.time_ns()) + "@gmail.com", 20)
        db.session.add(user)
        db.session.commit()
        return str(time.time_ns())

    def put(self, id):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        pass


class UserList(Resource):

    def get(self):
        users = UserDB.query.all()
        return Serializer.serialize_list(users)
        # pass


    def post(self):
        pass


