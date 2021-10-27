import krakenex
#from pykrakenapi import KrakenAPI
from data import kraken_api_key, kraken_api_private_key

class KrakenBot:
    def __init__(self):
        return
    
if __name__ == "__main__":
    k = krakenex.API(key = kraken_api_key, secret = kraken_api_private_key)
    print(k.query_private('Balance'))
