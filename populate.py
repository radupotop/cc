#!/usr/bin/env python3
#
# Populate db

from app import *
from datetime import datetime

with app.app_context():
    db.create_all()

    # Banks
    BRD = Banks(
        bank_name='BRD GSG',
        long_name='Banca Romana pentru Dezvoltare',
        country='RO'
    )
    BT = Banks(
        bank_name='BT',
        long_name='Banca Transilvania',
        country='RO'
    )
    ING = Banks(
        bank_name='ING',
        country='RO'
    )
    RAIF = Banks(
        bank_name='Raiffeisen',
        country='RO'
    )


    # Cards
    brd_cvt = Cards(
        bank=BRD,
        card_name='Cum Vrei Tu',
        type='Mastercard',
        currency='RON',
        interest_rate=14.72,
        interst_free_period=60,
        minimum_repayment_percent=2,
        max_credit_limit=22000,
        eligibility_employment_months=3,
        promotion='15% cashback la magazinele partenere: Emag, Decathlon, Casa Rusu, Praktiker, etc.',
        interest_fee_installments=12,
        internet_banking='MyBRD Net, MyBRD Mobile pe Android si iOS',
        is_contactless=True,
        offer_url='https://www.brd.ro/persoane-fizice/carduri/carduri-de-credit/cardul-de-credit-cumvreitu',
        renew_years=3,
        last_update=datetime.utcnow(),
    )

    bt_star_forte = Cards(
        bank=BT,
        card_name='Star Forte',
        type='Mastercard',
        currency='RON',
        interest_rate=24.00,
        interst_free_period=56,
        credit_limit_comment='De pana la 5 ori venitul lunar, maximum echivalentul a 5000 EUR in RON',
        minimum_repayment_percent=10,
        minimum_repayment='10%, intre 1 si 25 a lunii',
        opening_fee = 0,
        yearly_fee = 25,
        eligibility_employment_months=12,
        offer_url='http://www.starbt.ro/',
        rewards='Puncte Star - 1 punct = 1 leu, 8500 magazine partenere',
        interest_fee_installments=12,
        renew_years=5,
        is_contactless=True,
        allows_additional_cards=True,
        other_fees='http://www.starbt.ro/files/star-forte/comisioane_star_forte.pdf',
        last_update=datetime.utcnow(),
    )

    ing_cc = Cards(
        bank=ING,
        card_name='Credit Card',
        currency='RON',
        max_credit_limit=35000,
        renew_years=5,
        eligibility_employment_months=3,
        eligibility_min_salary=1500,
        eligibility='Venit minim 1500 RON, Minim un an vechime in munca si minim 3 luni vechime la ultimul angajator, fara intreruperi mai mari de o luna in ultimul an',
        interest_rate=20.83,
        interst_free_period=45,
        rewards='12 rate fara dobanda, 24 sau 36 rate cu 12% dobanda',
        interest_fee_installments=12,
        minimum_repayment_percent=5,
        minimum_repayment_sum=50,
        minimum_repayment='5%, 10% sau 15%, minim 50 RON, pe data de 5, 15 sau 25 ale lunii',
        is_contactless=False,
        allows_additional_cards=False,
        offer_url='https://www.ing.ro/ingb/persoane-fizice/credite/credit-card.html',
        sms_notif='Plati peste 300 RON',
        last_update=datetime.utcnow(),
    )

    raif_cc = Cards(
        bank=RAIF,
        card_name='Cardul Standard',
        currency='RON',
        type='Mastercard',
        min_credit_limit=700,
        max_credit_limit=20000,
        interest_rate=20.28,
        eligibility_employment_months=3,
        eligibility='Minim 3 luni vechime la ultimul loc de munca, 1 an vechime in piata muncii, Venit minim de 150 EUR pe familie',
        interst_free_period=56,
        is_contactless=True,
        allows_additional_cards=True,
        minimum_repayment_percent=5,
        minimum_repayment='5%, pe data de 7, 15, 22 ale lunii',
        rewards='puncte Multishop - 1 punct = 1 leu',
        interest_fee_installments=12,
        offer_url='https://www.raiffeisen.ro/persoane-fizice/produsele-noastre/credite/carduri-de-cumparaturi/cardul-de-cumparaturi-standard/',
        opening_fee=0,
        yearly_fee=40,
        default_charges='Plata intarziata: 20 RON',
        additional_charges='Interogare ATM propriu: 0.75 RON, Interogare ATM alte banci: 2.5 RON',
        travel_insurance='Travel insurance',
        purchase_protection=45,
        last_update=datetime.utcnow(),
    )


    # Add and commit

    # db.session.add(BRD)
    # db.session.add(brd_cvt)

    # db.session.add(BT)
    # db.session.add(bt_star_forte)

    # db.session.commit()
