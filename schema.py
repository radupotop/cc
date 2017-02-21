# https://flask-marshmallow.readthedocs.io/en/latest/

from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import ModelSchema
from model import *

ma = Marshmallow()

class BankSchema(ma.Schema):
    class Meta:
        model = Banks
        fields = ('id', 'slug', 'bank_name', 'country')

class CardTypesSchema(ma.Schema):
    class Meta:
        model = CardTypes
        fields = ('id', 'type_name', 'digits')

class CardsSchema(ma.Schema):
    class Meta:
        model = Cards
        fields = (
            'id',
            'slug',
            'card_name',
            'type',
            'bank',
            'currency',
            'interest_rate',
            'opening_fee',
            'monthly_fee',
            'last_update',
        )

    type = fields.Nested(CardTypesSchema())
    bank = fields.Nested(BankSchema())
