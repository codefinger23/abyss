# -*- coding: utf-8 -*-

from flask import Flask
from app.models import User

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route('/')
def hello_world():
    # User.insert(account="liuxiaodong11")
    result = User.get_by()
    print result
    return result

if __name__ == '__main__':
    app.run()
