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
            'bank',
            'card_name',
            'type',
            'currency',
            'interest_rate',
            'interest_free_days',
            'minimum_repayment_percent',
            'max_credit_limit',
            'opening_fee',
            'yearly_fee',
            'eligibility_employment_months',
            'promotion',
            'interest_free_installments',
            'internet_banking',
            'is_contactless',
            'offer_url',
            'renew_years',
            'allows_additional_cards',
            'balance_transfer',
            'balance_transfer_interest_rate',
            'last_update',
        )

    type = fields.Nested(CardTypesSchema())
    bank = fields.Nested(BankSchema())
