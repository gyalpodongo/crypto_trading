from coinbase.wallet.client import Client
from time import sleep
from data import api_key, api_secret

def percentage_change(a : float,b: float) -> float:
    """
    Takes two floats and returns their percentage change
    """
    return (a-b)/b * 100

