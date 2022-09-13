from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class AddressInputSchema(Schema):
  """ /api/hello - POST

  Parameters:
    - street (str)
    - city (str)
    - zipcode (int)
  """
  # the 'required' argument ensures the field exists
  street = fields.Str(required=True, validate=Length(max=200))
  city = fields.Str(required=True)
  zipcode = fields.Str(required=True)

class PersonInputSchema(Schema):
  """ /api/hello - POST

  Parameters:
    - fname (str)
    - lname (str)
    - age (int)
  """
  # the 'required' argument ensures the field exists
  fname = fields.Str(required=True, validate=Length(max=60))
  lname = fields.Str(required=True)
  age = fields.Int(required=True, validate=Range(min=1, max=99))
  address = fields.Nested(AddressInputSchema)

