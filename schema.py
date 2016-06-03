from marshmallow import Schema, fields
from marshmallow_sqlalchemy import ModelSchema

class BankSchema(ModelSchema):
    id = fields.Int()
    bank_name = fields.Str()
    bank_country = fields.Str()

class CardsSchema(ModelSchema):
    id = fields.Int()
    name = fields.Str()
    bank_id = fields.Int()
    currency = fields.Str()
    interest_rate = fields.Int()
    monthly_fee = fields.Int()

    # class Meta:
    #     model = Mdl.Cards

# schema = BankSchema()
# result = schema.dump(Banks)
