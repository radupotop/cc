#!/usr/bin/env python3

from flask import Flask, jsonify
from model import *
from schema import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cc.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/banks', methods=['GET'])
def getBanks():

    sch = BankSchema()

    return jsonify([ sch.dump(bank).data for bank in Banks.query.all() ])


@app.route('/cards', methods=['GET'])
def getCards():

    sch = CardsSchema()

    return jsonify([ sch.dump(c).data for c in Cards.query.all() ])


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 8080)
