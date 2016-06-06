from marshmallow import Schema, fields
# from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
from model import *

ma = Marshmallow()

class BankSchema(ma.Schema):
    id = fields.Str()
    class Meta:
        model = Banks
        fields = ('id', 'bank_name', 'bank_country')

class CardsSchema(ma.Schema):
    class Meta:
        model = Cards
        fields = ('id', 'name', 'bank_id', 'currency')
