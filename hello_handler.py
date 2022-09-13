from flask import jsonify, Blueprint, request, abort
from hello_service import HelloService
from validators.person_schema import PersonInputSchema

hellohandler = Blueprint('hello_handler', __name__)

@hellohandler.route('/', methods=["GET"])
def hello():
  service = HelloService()
  resp = service.getHelloForStranger()
  return resp

@hellohandler.route('/', methods=["POST"])
def hello_to_person():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    json = request.json
  else:
    return 'Content-Type not supported!'
  errors = PersonInputSchema().validate(json)
  print(errors)
  if errors:
    raise Exception(errors)
  return json

@hellohandler.route('/<string:name>', methods=["GET"])
def hello_name(name):
  service = HelloService()
  resp = service.getHelloForUser(name)
  return resp