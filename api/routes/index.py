from flask import jsonify

def register(api):
    @api.route('/', methods=[ 'GET' ])
    def index():
        return jsonify({ 'message': 'Hello, Flask!' })