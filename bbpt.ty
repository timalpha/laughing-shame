# -*- coding: utf-8 -*-
""" Bitstamp bitcoin price ticker
    Using json and pusherclient
"""
import json
import pusherclient
import time
import logging

global pusher

PUSHER_KEY = "de504dc5763aeef9ff52"

def trade_callback(data):
    price_data = json.loads(data)       # Convert json string to dict
    print(price_data["price"])

def connect_handler(data):
  channel = pusher.subscribe('live_trades')
  channel.bind('trade', trade_callback)

if __name__ == '__main__':
  pusher = pusherclient.Pusher(PUSHER_KEY)
  pusher.connection.logger.setLevel(logging.WARNING)
  pusher.connection.bind('pusher:connection_established', connect_handler)
  pusher.connect()

  while True:
    time.sleep(1)
