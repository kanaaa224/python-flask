from flask import Flask

def create():
    api = Flask(__name__)

    from .routes import register

    register(api)

    return api