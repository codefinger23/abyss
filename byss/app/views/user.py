# encoding=utf-8
from app.extensions.restplus import extension as api
from app.models import User
from flask_restplus import Resource, fields, Namespace

ns = Namespace("users", description="Users CURD api.")

user_model = ns.model('UserModel', {
    "id": fields.Integer(description="用户唯一标识"),
    "account": fields.String(description="用户账号"),
    "nickname": fields.String(description="用户昵称"),
    "password": fields.String(description="用户密码"),
    "type": fields.String(required=True, description="请求类型标识"),
})

@ns.route("")
class UserAPI(Resource):
    
    @ns.doc('get user info')
    @ns.marshal_with(user_model)
    def get(self):
        result = User.get_by()
        print result
        return result

    def post(self):
        return {"status": "OK"}

    def put(self):
        return "OK"

    def delete(self):
        return "OK"