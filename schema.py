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

class CardsSchema(ma.Schema):
    class Meta:
        model = Cards
        fields = (
        	'id',
        	'slug',
        	'card_name',
        	'bank_id',
        	'type',
        	'currency',
        	"interest_rate",
        	"opening_fee",
        	"monthly_fee",
        )
