from flask import Flask, jsonify
from flask_restful import Resource, Api
from hello_handler import hellohandler

app = Flask(__name__)

def _initialize_errorhandlers(app):
    '''
    Initialize error handlers
    '''
    from error_handlers import errors
    app.register_blueprint(errors)

def main():
    api = Api(app)
    app.register_blueprint(hellohandler, url_prefix='/api/hello')
    _initialize_errorhandlers(app)
    app.run(debug=False, port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()