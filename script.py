from coinbase.wallet.client import Client
from time import sleep
from data import api_key, api_secret

#Some coinbase guidance https://developers.coinbase.com/docs/wallet/guides/buy-sell

def percentage_change(a : float,b: float) -> float:
    """
    Takes two string numbers and returns their percentage change
    """
    return (float(b)-float(a))/float(a) * 100

#setting our client to link our account to our code
client = Client(api_key,api_secret)
#payment_method = client.get_payment_methods()[0] #Gets main form of payment from your coinbase account

#Following lines get inputs from the user such as the currency they use, the limit order and the amount spent

#API does not seem to support other currencies than USD
#currency_code= str(input("What currency are you using? (Please enter in 3 character valid format e.g. USD): "))

currency_code = "USD"



user_limit_order = float(input(f"Enter a price for your bitcoin limit order in {currency_code}: "))

user_amount_spent = float(input(f"Enter how much you want to spend in {currency_code}: "))

t = int(input("How often do you want tochekc the percentage gain loss? Enter integer in seconds: "))

start_price = client.get_spot_price(currency = currency_code)

while True:
    #Reset current values and finds percentage changes
    buy_price = client.get_buy_price(currency = currency_code)
    percentage_gainloss = percentage_change(start_price.amount, buy_price.amount)

    #print bitcoin current price and percentage change

    print(f"Bitcoin is {buy_price.amount} \nPercent change in last {t} seconds: {round(percentage_gainloss,3)} %")
    #answer = input("Do you want to buy? (Enter Y or N) ").lower()
    answer = "y"

    if(float(buy_price.amount) <= user_limit_order) and answer == "y":
        #buy = client.buy(amount=str(user_amount_spent / float(buy_price.amount)), currency=currency_code, payment_method = payment_method.id )

        print(f" Bought bitcoin ({currency_code}) {user_amount_spent} or {user_amount_spent/ float(buy_price.amount)} bitcoin at {buy_price.amount} ({currency_code})")
        break
    else:
        print(f"Checking again after {t} seconds")

    #Checks again after t seconds
    sleep(t) 

    #Update start_price
    start_price = buy_price