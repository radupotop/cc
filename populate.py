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
        type='Mastercard',
        currency='RON',
        interest_rate=14.72,
        interst_free_period='60 days',
        minimum_repayment='2%',
        max_credit_limit=22000,
        eligibility='Must be employed for 3 months minimum.',
        promotion='15% cashback: Emag, Decathlon, Casa Rusu, Praktiker',
        internet_banking='MyBRD Net, MyBRD Mobile',
        is_contactless=True,
        offer_url='https://www.brd.ro/persoane-fizice/carduri/carduri-de-credit/cardul-de-credit-cumvreitu',
        renew_years=3,
    )

    bt_star_forte = Cards(
        card_name='BT Star Forte',
        type='Mastercard',
        currency='RON',
        interest_rate=24.00,
        interst_free_period='56 days',
        credit_limit_comment='Pana la de 5 ori salariul, maximum echivalentul a 5000 EUR in RON',
        minimum_repayment='10%, intre 1 si 25 a lunii',
        opening_fee = 0,
        yearly_fee = 25,
        eligibility='1 an angajare',
        offer_url='http://www.starbt.ro/',
        promotion='12 rate fara dobanda, 8500 magazine partenere, puncte Star, 1 punct = 1 leu',
        renew_years=5,
        is_contactless=True,
        allows_additional_cards=True,
        other_fees='http://www.starbt.ro/files/star-forte/comisioane_star_forte.pdf',

    )
