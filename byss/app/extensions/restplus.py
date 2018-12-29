# encoding = utf-8

from flask import Blueprint
from flask_restplus import Api

class NewAPI(Api):
    def __init__(self):
        super(NewAPI, self).__init__(title="abyss", description="abyss CURD api.", doc="/doc")
        
    def init_app(self, app):
        api_blueprint = Blueprint("open_api", __name__, url_prefix="/api")
        super(NewAPI, self).init_app(api_blueprint)
        app.register_blueprint(api_blueprint)

extension = NewAPI()