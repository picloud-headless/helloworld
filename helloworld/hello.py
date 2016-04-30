# http://flask-restful-cn.readthedocs.org/en/0.3.4/quickstart.html
from flask import Flask
from flask_restful import Resource, Api


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Hello(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(HelloWorld, '/')
