# Coinbase Bitcoin Basic Bot
Basic Trading Algorithms for cryptocurrencies using different exchanges API

## Installation

1. Install the coinbase api typing in your command prompt/terminal `pip install coinbase` or `pip3 install coinbase`.

2. Create a file called `data.py` in the same folder as `script.py` where you can create two variables:
   - `api_key` which will be a string containing your coinbase api key.
   - `api_secret` which will be a string containing your coinbase api secret.

3. Uncomment these lines to start making actual purchases:
   - `#payment_method = client.get_payment_methods()[0] #Gets main form of payment from your coinbase account`
   - `#buy = client.buy(amount=str(user_amount_spent / float(buy_price.amount)), currency=currency_code, payment_method = payment_method.id )`

4. You are good to go to buy your BTC!

