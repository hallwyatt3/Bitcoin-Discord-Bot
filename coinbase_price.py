import requests
import json

def price():
    price = requests.get('https://api.pro.coinbase.com/products/BTC-USD/ticker')
    rate = price.json()['price']
    return float(rate)