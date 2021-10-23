from coinbase.wallet.client import Client
from data import coinbase_api_key, coinbase_api_secret
from time import sleep

#Some coinbase guidance https://developers.coinbase.com/docs/wallet/guides/buy-sell

class Coinbot:
    def __init__(self):
        """
            Initialization method for Coinbase bot used for trading, buying and selling bitcoin.
            
            It will require your api key and api secret from data.py in the same folder as this file each saved there
            as 'coinbase_api_key' and 'coinbase_api_secret'.
        """
        self.client = Client(coinbase_api_key,coinbase_api_secret)
        #payment_method =  #Gets main form of payment from your coinbase account
        self.payment_method = self.client.get_payment_methods()[0]

        #API does not seem to support other currencies than USD
        #currency_code= str(input("What currency are you using? (Please enter in 3 character valid format e.g. USD): "))
        self.currency_code = "USD"

    def percentage_change(self,a : str,b: str) -> float:
        return (float(b)-float(a))/float(a) * 100

    def buy(self,user_amount_spent,buy_price):
        #self.client.buy(amount=str(user_amount_spent / float(buy_price.amount)), currency=self.currency_code, payment_method = self.payment_method.id )
        print(f" Bought bitcoin ({self.currency_code}) {user_amount_spent} or {user_amount_spent/ float(buy_price.amount)} bitcoin at {buy_price.amount} ({self.currency_code})")
    
    def trade(self, interactive = False):
        #Following lines get inputs from the user such as the currency they use, the limit order and the amount spent
        user_limit_order = float(input(f"Enter a price for your bitcoin limit order in {self.currency_code}: "))
        user_amount_spent = float(input(f"Enter how much you want to spend in {self.currency_code}: "))
        time = int(input("How often do you want to check the percentage gain loss? Enter integer in seconds: "))
        start_price = self.client.get_spot_price(currency = self.currency_code)
        
        while True:
            buy_price = self.client.get_buy_price(currency = self.currency_code)
            percentage_gainloss = self.percentage_change(start_price.amount, buy_price.amount)
            print(f"Bitcoin is {buy_price.amount} \nPercent change in last {time} seconds: {round(percentage_gainloss,3)} %")
            if interactive:
                answer = input("Do you want to buy? (Enter Y or N) ").lower()
            else:
                answer = "y"

            if(float(buy_price.amount) <= user_limit_order) and answer == "y":
                self.buy(user_amount_spent,buy_price)
                break
            sleep(time) 
            start_price = buy_price


            




