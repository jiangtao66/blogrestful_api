#!./venv/bin/python
from flask_script import Manager, Shell
from flask import Flask
from flask_restful import Api
from app.main import main as main_blueprint
from app.main.views import HelloWorld

app = Flask(__name__)

app.register_blueprint(main_blueprint)
api = Api(app)
api.add_resource(HelloWorld, '/')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
