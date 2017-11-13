#!./venv/bin/python
from flask_script import Manager, Shell
from flask import Flask

app = Flask(__name__)

manager = Manager(app)


def make_shell_context():
    return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
