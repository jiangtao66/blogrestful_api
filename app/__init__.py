from  flask import Flask
from flask_restful import Api
from app.main import main as main_blueprint
from app.main.views import HelloWorld, TodoSimple

api = Api()

def create_app():
    app = Flask(__name__)
    api.add_resource(HelloWorld, '/')
    api.add_resource(TodoSimple, '/<string:todo_id>')
    api.init_app(app)
    return app