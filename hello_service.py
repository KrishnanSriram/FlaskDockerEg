from flask import jsonify

class HelloService:
  def init(self):
    print('HelloService init invoked')

  def getHelloForStranger(self):
    return jsonify({
      'message':'Hello from bulebrint stranger!!'
    })

  def getHelloForUser(self, name):
    return jsonify({
      'message':'Hello from bulebrint {}!!'.format(name)
    })