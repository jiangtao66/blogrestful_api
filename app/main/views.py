from flask_restful import Resource
from flask import request


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

todo = {}
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todo[todo_id]}

    def put(self, todo_id):
        todo[todo_id] = request.args.get('data')
        return {todo_id: todo[todo_id]}
