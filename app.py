#!/usr/bin/env python3
#
# Define routes and main application entry point

from flask import Flask, jsonify
from model import *
from schema import *
from pprint import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cc.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/banks', methods=['GET'])
def getBanks():

    sch = BankSchema()
    data = [ sch.dump(bank).data for bank in Banks.query.all() ]
    
    return jsonify(data)


@app.route('/cards', methods=['GET'])
def getCards():

    sch = CardsSchema()
    data = [ sch.dump(c).data for c in Cards.query.all() ]
    
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 8080)
