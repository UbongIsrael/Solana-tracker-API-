from tokenmethods import get_token_details, get_token_price, get_holders_info, get_chart_data, get_top_traders, get_stats,get_token_pool_stats
from walletmethods import get_latest_trades,get_token_pnl,get_wallet_tokens

#TOKEN CLASS FOR EASY QUERYING OF METHODS
class Token:
    def __init__(self, token_address:str) -> None:
        self.token_address = token_address

    def get_info(self):
        token_info = get_token_details(self.token_address)
        return token_info

    def get_price(self):
        price = get_token_price(self.token_address)
        return price
    
    def get_holders(self):
        holder_info = get_holders_info(self.token_address)
        return holder_info
    
    def get_chart_OLCVH(self):
        olchv_data = get_chart_data(self.token_address)
        return olchv_data
    
    def get_top_100_traders(self):
        top_100_data = get_top_traders(self.token_address)
        return top_100_data
    
    def get_token_stats(self):
        token_stats = get_stats(self.token_address)
        return token_stats
    
    def get_token_pool_stat(self, pool_address):
        # pool_address = input("Input pool address")
        token_pool_details = get_token_pool_stats(self.token_address,pool_address)
        return token_pool_details


# WALLET CLASS FOR EASY METHOD QUERYING

class Wallet:
    def __init__(self, wallet_address:str) -> None:
        self.wallet_address = wallet_address

    def get_tokens(self):
        wallet_tokens = get_wallet_tokens(self.wallet_address)
        return wallet_tokens
    
    def get_trades(self):
        latest_trades = get_latest_trades(self.wallet_address)
        return latest_trades
    
    def get_token_pnl_data(self,token_address):
        pnl_data = get_token_pnl(self.wallet_address,token_address)
        return pnl_data

