#!/usr/bin/env python2

from flask import Flask, jsonify
from model import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cc.db'
db.init_app(app)

@app.route('/banks', methods=['GET'])
def get():

    return jsonify([ bank.to_dict() for bank in Banks.query.all() ])
    
if __name__ == '__main__':
  app.debug = True
  app.run('0.0.0.0', 8080)
