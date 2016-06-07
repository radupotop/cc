#!/usr/bin/env python2
#
# Populate db

from app import *

with app.app_context():
    db.create_all()
    
    db.session.add(Banks('BRD', 'RO'))
    db.session.add(Banks('Bancpost', 'RO'))
    db.session.add(Banks('ING', 'RO'))
    db.session.add(Banks('Unicredit', 'RO'))

    db.session.add(Cards(card_name='AMEX', bank_id=1, currency='GBP'))

    db.session.commit()
