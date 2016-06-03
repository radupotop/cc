#!/usr/bin/env python2

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import *

app = Flask(__name__)

@app.route('/banks', methods=['GET'])
def get():
    
    result = []
    
    for bank in Banks.query.all():
        result.append(bank.to_dict())
    
    return jsonify({
        'banks': result
    })

if __name__ == '__main__':
  app.debug = True
  app.run('0.0.0.0', 8080)
