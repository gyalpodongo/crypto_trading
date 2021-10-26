# Coinbase Bitcoin Basic Bot
Basic Coinbase Bot for trading Bitcoin

## Setting Up

1. Create a file called `data.py` in the same folder as `coinbase_bot.py` where you can create two variables:
   - `coinbase_api_key` which will be a string containing your coinbase api key.
   - `coinbase_api_secret` which will be a string containing your coinbase api secret.

2. Uncomment this line to start making actual purchases in the buy method:
   - `#self.client.buy(amount=str(user_amount_spent / float(buy_price.amount)), currency=self.currency_code, payment_method = self.payment_method.id )`
   
3. You are good to go to buy your BTC with coinbase!