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
PRICE_LIST = [0]
DISPLAY_MSG = "USD/BTC"
# Console colors
WHITE = '\033[0m' # white (normal)
RED = '\033[31m' # red
GREEN = '\033[32m' # green
# ORANGE = '\033[33m' # orange
BLUE = '\033[34m' # blue
# PURPLE = '\033[35m' # purple
# CYAN = '\033[36m' # cyan
# GRAY = '\033[37m' # gray

def trade_callback(data):
  price_data = json.loads(data)       # Convert json string to dict

  PRICE_LIST.append(price_data["price"])

  if PRICE_LIST[-1] > PRICE_LIST[-2]:
    print(WHITE, DISPLAY_MSG, GREEN, PRICE_LIST[-1], WHITE)
  elif PRICE_LIST[-1] < PRICE_LIST[-2]:
    print(WHITE, DISPLAY_MSG, RED, PRICE_LIST[-1], WHITE)
  else:
    print(WHITE, DISPLAY_MSG, BLUE, PRICE_LIST[-1], WHITE)

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
