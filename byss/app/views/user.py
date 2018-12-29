# encoding=utf-8
from app.extensions.restplus import extension as api
from app.models import User
from flask_restplus import Resource, fields, Namespace

ns = Namespace("users", description="Users CURD api.")

@ns.route("")
class UserAPI(Resource):
    def get(self):
        User.get_by()
        return {"user": 1}

    def post(self):
        return {"status": "OK"}

    def put(self):
        return "OK"

    def delete(self):
        return "OK"