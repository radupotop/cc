#!/usr/bin/env python3
#
# Populate db

from app import *

with app.app_context():
    db.create_all()

    bancpost = Banks.query.filter_by(bank_name='Bancpost_').first()
    # db.session.add(bancpost)
    
    # db.session.add(Banks('Bancpost', 'RO'))
    # db.session.add(Banks('ING', 'RO'))
    # db.session.add(Banks('Unicredit', 'RO'))

    amex = Cards(card_name='AMEX', currency='GBP')
    amex.bank = bancpost

    db.session.add(amex)

    db.session.commit()


    brd_cum_vrei_tu = Cards(
        card_name='BRD Cum vrei tu',
        currency='RON',
        interest_rate=14.72,
        interst_free_period='60 days',
        minimum_repayment='2%',
        max_credit_limit=22000,
        eligibility='Must be employed for 3 months minimum.'
    )
