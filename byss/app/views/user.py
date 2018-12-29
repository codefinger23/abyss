# encoding=utf-8

@api.route("/user")
class User(Resource):
    def get(self):
        return {"user": 1}
    def post(self):
        return {"status": "OK"}