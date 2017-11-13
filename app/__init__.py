from  flask import Flask
from flask_restful import Api
from app.main import main as main_blueprint
from app.main.views import HelloWorld

api = Api()

def create_app():
    app = Flask(__name__)
    api.add_resource(HelloWorld, '/')
    api.init_app(app)
    return app