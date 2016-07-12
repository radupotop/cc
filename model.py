# http://flask-sqlalchemy.pocoo.org/2.1/

import utils
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define our models

class Banks(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    slug = db.Column(db.String(40), unique=True)
    bank_name = db.Column(db.String(40))
    long_name = db.Column(db.String(255))
    country = db.Column(db.String(2))
    cards = db.relationship('Cards', backref=db.backref('bank'))

    def __repr__(self):
        return '<Bank %s from %s>' % (self.bank_name, self.country)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

        self.slug = utils.slugify(self.bank_name + '-' + self.country)


# CreditCard Model
class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)
    slug = db.Column(db.String(255))
    # ref bank

    card_name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('VISA', 'Mastercard', 'Amex', 'JCB'))
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

    opening_fee = db.Column(db.Float)
    monthly_fee = db.Column(db.Float)
    yearly_fee = db.Column(db.Float)
    other_fees = db.Column(db.String(255))

    # Cards have a minimum repayment amount
    minimum_repayment_percent = db.Column(db.Integer)
    minimum_repayment_sum = db.Column(db.Float)
    minimum_repayment = db.Column(db.String(60))

    additional_charges = db.Column(db.Text) # dormancy fee, statement copy,
    foreign_usage = db.Column(db.Text) # eg. non-sterling fee
    default_charges = db.Column(db.Text) # late payment, over-limit, returned payment

    min_credit_limit = db.Column(db.Integer)
    max_credit_limit = db.Column(db.Integer)
    credit_limit_comment = db.Column(db.String(255))

    # Renews every X years
    renew_years = db.Column(db.Integer)
    allows_additional_cards = db.Column(db.Boolean)

    # Most cards offer some sort of promotion,
    # like the first three months interest free, or more cashback.
    promotion = db.Column(db.Text)
    promo_duration = db.Column(db.Integer) # promotion duration in months
    rewards = db.Column(db.Text) # regular rewards after the promotion period has expired
    
    interest_fee_installments = db.Column(db.Integer) # number of installments
    travel_insurance = db.Column(db.String(255)) # some cards offer insurance on travel
    purchase_protection = db.Column(db.Integer) # number of days for purchase protection

    # Most cards have eligibility criteria
    eligibility_employment_months = db.Column(db.Integer) # minimum employment period in months
    eligibility_min_salary = db.Column(db.Float)
    eligibility = db.Column(db.Text) # additional description of eligibility criteria

    internet_banking = db.Column(db.String(255))
    sms_notif = db.Column(db.String(255))
    is_contactless = db.Column(db.Boolean())

    offer_url = db.Column(db.String(255))

    comments = db.Column(db.Text)

    last_update = db.Column(db.DateTime)

    def __repr__(self):
        return '<Card %s from %s in %s>' % (self.card_name, self.bank.bank_name, self.currency)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

        self.slug = utils.slugify(self.bank.bank_name + '-' + self.card_name)
