# -*- coding: utf-8 -*-

from flask_script import Manager, Server, Shell, Command, Option
from flask_script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand

from app.main import app
from app.lib.database import db


manager = Manager(app)

is_sqlite = app.config.get('SQLALCHEMY_DATABASE_URI').startswith('sqlite:')
print app.config.get('SQLALCHEMY_DATABASE_URI')
migrate = Migrate(app, db, render_as_batch=is_sqlite)


def _make_context():
    return dict(app=app, db=db)


class GunicornServer(Command):
    """Run the app within Gunicorn"""

    def run(self):
        from gunicorn.app.wsgiapp import WSGIApplication

        app = WSGIApplication()
        app.app_uri = 'manage:app'
        return app.run()


manager.add_command('db', MigrateCommand)
manager.add_command('url', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('server', Server(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 8888)))
manager.add_command('dev', Server(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 8888), use_debugger=True, threaded=True))
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("gunicorn", GunicornServer())

if __name__ == '__main__':
    manager.run()

