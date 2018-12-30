# -*- coding: utf-8 -*-

import pkgutil
from app import extensions,views
from app.lib.error_define import *
from app.models import User
from flask import Flask,session,request,redirect
from flask_restplus import Resource, Api

import json

app = Flask(__name__, instance_relative_config=True)

def init_config():
    """
    flask config
    config.py -> instance/config.py
    """
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

def init_before():
    @app.before_request
    def before_request():
        print request.path
        return

def init_error_handler():

    @app.errorhandler(ValidationError)
    def hanlde_validation(error):
        return res(code=203, msg=error.msg)

    @app.errorhandler(SupportError)
    def hanlde_support(error):
        return res(code=204, msg=error.msg)

    @app.errorhandler(PermissionError)
    def hanlde_permission(error):
        return res(code=205, msg=error.msg)

def load_extensions_dynamic():
    priority_chain = getattr(extensions, "priority_chain", [])
    blacklist = getattr(extensions, "blacklist", [])
    init_mod_list = []
    for name in priority_chain:
        try:
            _module = __import__("{0}.{1}".format(extensions.__name__, name), fromlist=[""])
        except ImportError:
            continue
        init_mod_list.append(_module)
    for _, name, _ in pkgutil.iter_modules(extensions.__path__):
        if name in priority_chain+blacklist:
            continue
        else:
            _module = __import__("{0}.{1}".format(extensions.__name__, name), fromlist=[""])
        init_mod_list.append(_module)
    
    for _module in init_mod_list:
        _type = "ignore"
        if hasattr(_module, "extension"):
            _type = "register"
            getattr(_module.extension, "init_app")(app)
        print "loading  {0:11}: {1:35} =>    {2}".format("extensions", _module.__name__, _type)

def register_api():
    init_view_list = []
    for _, name, _ in pkgutil.iter_modules(views.__path__):
        _view = __import__("{0}.{1}".format(views.__name__, name), fromlist=[""])
        init_view_list.append(_view)
    for _view in init_view_list:
        if hasattr(_view, "ns"):
            extensions.restplus.extension.add_namespace(_view.ns)
        print "register {0:11}: {1:35} =>    mounted".format("views", _view.__name__)

with app.app_context():
    init_config()
    init_before()
    init_error_handler()
    load_extensions_dynamic()
    register_api()

# api = Api(app, title="abyss", description="abyss CURD api.", doc="/doc")

@app.route('/')
def hello_world():
    result = "{}"
    User.insert(account="liuxiaodong")
    result = User.get_by()
    print json.dumps(result)
    return json.dumps(result)

