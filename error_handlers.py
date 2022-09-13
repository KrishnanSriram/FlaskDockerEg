from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.errorhandler(404)
def resource_not_found(e):
  print('{} in {} invoked'.format('resource_not_found', 'error_handlers'))
  return jsonify({
      'error': str(e)
  })

@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
  print('{} in {} invoked'.format('handle_unexpected_error', 'error_handlers'))
  status_code = 500
  success = False
  response = {
      'success': success,
      'error': {
          'type': 'UnexpectedException',
          'message': 'An unexpected error has occurred.',
          'detailedError': str(error)
      }
  }

  return jsonify(response), status_code