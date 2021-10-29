import krakenex
import time
#from pykrakenapi import KrakenAPI
from data import kraken_api_key, kraken_api_private_key

class KrakenBot:
    def __init__(self,currency="USD"):
        self.bot = krakenex.API(key = kraken_api_key, secret = kraken_api_private_key)
        self.currency = currency 

    def buy(self,data):
        return self.bot.query_private('AddOrder',data)
    def assetInfo(self):
        return self.bot.query_public("Assets")['result']
    def ticker(self,pair):
        return self.bot.query_public(f"Ticker?pair={pair}")
    
    
    def check_balance(self):
        try:
            result = self.bot.query_private('Balance')
        except:
            print("Error")
        if 'result' in result:
            return result['result']
        else:
            return result['error']
    
if __name__ == "__main__":
    k = KrakenBot()
    print(k.check_balance())
    print(k.assetInfo()['XXBT'])
    print(k.ticker("XBTGBP"))
