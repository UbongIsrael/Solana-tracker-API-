import requests
from config import KEY, handle_request

api_key = KEY
header = {"x-api-key": api_key}


#GET TOKENS HELD BY AN ADDRESS
def get_wallet_tokens(wallet_address):
    """
    Get all tokens in a wallet with current value in USD.
    """
    url = f"https://data.solanatracker.io/wallet/{wallet_address}"
    token_details = requests.get(url,headers=header)
    response = handle_request(token_details)
    return response if response else None


#GET LATESTS TRADES PERFORMED BY AN ADDRESS
def get_latest_trades(wallet_address):
    """
    Get the latest trades of a wallet.

    Query Parameters:
    - cursor (optional): Cursor for pagination
    """

    url = f"https://data.solanatracker.io/wallet/{wallet_address}/trades"
    token_details = requests.get(url,headers=header)
    response = handle_request(token_details)
    return response if response else None


#GET PNL FOR SPECIFIC TOKEN IN A WALLET
def get_token_pnl(wallet_address, token_address):
    """
    Get Profit and Loss data for a specific token in a wallet.
    """
    url = f"https://data.solanatracker.io/pnl/{wallet_address}/{token_address}"
    token_details = requests.get(url,headers=header)
    response = handle_request(token_details)
    return response if response else None


