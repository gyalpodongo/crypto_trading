
import sys
sys.path.append('./coinbase/')
from coinbase_bot import Coinbot

if __name__ == '__main__':
    bot = Coinbot()
    bot.trade_basic()