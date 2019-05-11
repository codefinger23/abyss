# encoding = utf-8

from flask import Blueprint
from flask_restplus import Api

class NewAPI(Api):
    def __init__(self):
        super(NewAPI, self).__init__(title="abyss", prefix="/api", description="abyss CURD api.", doc="/doc")
        
    def init_app(self, app):
        super(NewAPI, self).init_app(app)

extension = NewAPI()