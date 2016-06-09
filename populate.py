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
