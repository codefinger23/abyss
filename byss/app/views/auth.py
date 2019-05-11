# encoding=utf-8
from app.extensions.restplus import extension as api
from app.lib.error_define import *
from app.models import User
from flask_restplus import Resource, fields, Namespace, reqparse
from flask import abort

ns = Namespace("auth", description="auth about api.")

user_model = ns.model('UserModel', {
    "id": fields.Integer(description="用户唯一标识"),
    "account": fields.String(required=True, description="用户账号"),
    "nickname": fields.String(required=True, description="用户昵称"),
    "password": fields.String(required=True, description="用户密码"),
})

parser = reqparse.RequestParser()
parser.add_argument('account', type=str, help="注册账户，通常为邮箱")
parser.add_argument('nickname', type=str, help="用户昵称, 最长为12字节")
parser.add_argument('password', type=str, help="用户密码, 最长为16字节")
parser.add_argument('invite', type=str, help="邀请码，用户需要邀请码才允许注册")

@ns.route("")
class AuthAPI(Resource):

    @ns.doc('登录系统，记录登录态')
    @ns.marshal_with(user_model)
    def get(self):
        result = User.get_by()
        print result
        return result

    @ns.doc('注册为系统用户')
    @ns.expect(parser)
    def post(self):
        data = parser.parse_args()
        print "This is signup"
        print data
        abort(SupportError("邀请码过期"))
        return res({"status": "OK"})
