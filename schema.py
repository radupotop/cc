# https://flask-marshmallow.readthedocs.io/en/latest/

from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import ModelSchema
from model import *

ma = Marshmallow()

class BankSchema(ma.Schema):
    class Meta:
        model = Banks
        fields = ('id', 'bank_name', 'bank_country')

class CardsSchema(ma.Schema):
    class Meta:
        model = Cards
        fields = ('id', 'card_name', 'bank_id', 'currency')
