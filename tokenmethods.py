import requests
from config import KEY, handle_request


api_key = KEY
header = {"x-api-key": api_key}

def get_token_details(token_address:str):
    """
    Retrieve all information for a specific token.
    """
    url = f"https://data.solanatracker.io/tokens/{token_address}"
    token_details = requests.get(url,headers=header)
    response = handle_request(token_details)
    return response if response else None

def get_holders_info(token_address:str):
    """
    Get all holders for a specific token.
    """
    url = f"https://data.solanatracker.io/tokens/{token_address}/holders"
    token_details = requests.get(url,headers=header)
    response = handle_request(token_details)
    return response if response else None

def get_token_price(token_address:str):

    """
    Get price information for a single token.

    Query Parameters:
    - token (required): The token address
    """
    params = {"token": token_address}
    url = f"https://data.solanatracker.io/price"
    token_details = requests.get(url, params = params, headers=header)
    response = handle_request(token_details)
    return response if response else None

def get_chart_data(token_address:str):
    '''
    Get OLCVH (Open, Low, Close, Volume, High) data for charts.

    Query Parameters:

    - type (optional): Time interval (e.g., "1s", "1m", "1h", "1d")\n
    - time_from (optional): Start time (Unix timestamp in seconds)\n
    - time_to (optional): End time (Unix timestamp in seconds)
    '''

    url = f"https://data.solanatracker.io/chart/{token_address}"
    params = {"type":'optional....'}
    token_details = requests.get(url,headers=header,params=None) # Include the params parameter if you'll need it.
    response = handle_request(token_details)
    return response if response else None

def get_top_traders(token_address):
    """
    Get top 100 traders by PnL for a token.
    """
    url = f"https://data.solanatracker.io/top-traders/{token_address}"
    token_details = requests.get(url,headers=header) 
    response = handle_request(token_details)
    return response if response else None

def get_stats(token_address):
    """
    Get detailed stats for a token over various time intervals
    """
    url = f"https://data.solanatracker.io/stats/{token_address}"
    token_details = requests.get(url,headers=header) 
    response = handle_request(token_details)
    return response if response else None


def get_token_pool_stats(token_address, pool_address):
    """
    Get detailed stats for a token-pool pair over various time intervals.
    """
    url = f"https://data.solanatracker.io/stats/{token_address}/{pool_address}"
    token_details = requests.get(url,headers=header) 
    response = handle_request(token_details)
    return response if response else None

