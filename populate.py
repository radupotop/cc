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


    brd_cvt = Cards(
        card_name='BRD Cum vrei tu',
        type='Mastercard',
        currency='RON',
        interest_rate=14.72,
        interst_free_period=60,
        minimum_repayment='2%',
        max_credit_limit=22000,
        eligibility='Must be employed for 3 months minimum.',
        promotion='15% cashback: Emag, Decathlon, Casa Rusu, Praktiker',
        internet_banking='MyBRD Net, MyBRD Mobile pe Android si iOS',
        is_contactless=True,
        offer_url='https://www.brd.ro/persoane-fizice/carduri/carduri-de-credit/cardul-de-credit-cumvreitu',
        renew_years=3,
    )

    bt_star_forte = Cards(
        card_name='BT Star Forte',
        type='Mastercard',
        currency='RON',
        interest_rate=24.00,
        interst_free_period=56,
        credit_limit_comment='De pana la 5 ori venitul lunar, maximum echivalentul a 5000 EUR in RON',
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

    ing_cc = Cards(
        card_name='ING Credit Card',
        currency='RON',
        max_credit_limit='35000',
        renew_years=5,
        eligibility='Venit minim 1500 RON, Minim un an vechime in munca si minim 3 luni vechime la ultimul angajator, fara intreruperi mai mari de o luna in ultimul an',
        interest_rate=20.83,
        interst_free_period=45
        promotion='12 rate fara dobanda, 24 sau 36 rate cu 12% dobanda',
        minimum_repayment='5%, 10% sau 15%, minim 50 RON, pe data de 5, 15 sau 25 ale lunii',
        is_contactless=False,
        allows_additional_cards=False,
        offer_url='https://www.ing.ro/ingb/persoane-fizice/credite/credit-card.html',
        sms_notif='Plati peste 300 RON',
    )
