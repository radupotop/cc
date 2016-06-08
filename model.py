# http://flask-sqlalchemy.pocoo.org/2.1/

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define our models

class Banks(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bank_name = db.Column(db.String(40), unique=True)
    bank_country = db.Column(db.String(2))
    cards = db.relationship('Cards', backref=db.backref('bank'))

    def __repr__(self):
        return '<Bank %s from %s>' % (self.bank_name, self.bank_country)
    
    def __init__(self, name, country):
        self.bank_name = name
        self.bank_country = country



# CreditCard Model
class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)

    card_name = db.Column(db.String(255), nullable=False)
    currency = db.Column(db.String(3))

    # Usually there's a basic annual interest rate,
    # and a higher rate for cash withdrawals
    interest_rate = db.Column(db.Float) # APR
    # Some cards have a variable rate
    max_interest_rate = db.Column(db.Float)

    balance_transfer_interest_rate = db.Column(db.Float)
    cash_withdraw_interest_rate = db.Column(db.Float)
    cash_withdraw_fee = db.Column(db.String(40))
    interest_free_period = db.Column(db.Integer) # in days if ballance is paid in full
    
    monthly_fee = db.Column(db.Float)
    yearly_fee = db.Column(db.Float)

    minimum_repayment = db.Column(db.String(60))

    additional_charges = db.Column(db.Text) # dormancy fee, statement copy, 
    foreign_usage = db.Column(db.Text) # eg. non-sterling fee
    default_charges = db.Column(db.Text) # late payment, over-limit, returned payment

    min_credit_limit = db.Column(db.Integer)
    max_credit_limit = db.Column(db.Integer)

    # Most cards offer some sort of promotion, 
    # like the first three months interest free, or more cashback.
    promotion = db.Column(db.String(255))
    promo_duration = db.Column(db.Integer) # promotion duration in months
    rewards = db.Column(db.Text) # regular rewards after the promotion period has expired
    insurance = db.Column(db.Text) # some cards offer insurance on travel or purchases

    eligibility = db.Column(db.Text)

    offer_url = db.Column(db.String(255))

    comments = db.Column(db.Text)

    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return '<Card %s from %s in %s>' % (self.card_name, self.bank_id, self.currency)

    def __init__(self, bank_id, card_name, currency):
        self.bank_id = bank_id
        self.card_name = card_name
        self.currency = currency
