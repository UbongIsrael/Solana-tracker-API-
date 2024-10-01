from config import print_json
from token_1 import Wallet,Token


def token_attr():
    # Ask user for token address
    token_address = input("Enter the token address: ")
    
    # Create an instance of Token
    token_obj = Token(token_address)

    # Get all methods of the object excluding private ones
    methods = [method for method in dir(token_obj) if callable(getattr(token_obj, method)) and not method.startswith("_")]

    # Display the methods
    print("\nAvailable methods:")
    for i, method in enumerate(methods, 1):
        print(f"{i}. {method}")

    # Ask the user to choose a method
    choice = int(input("\nEnter the number of the method you want to call: ")) - 1

    # Call the selected method
    if 0 <= choice < len(methods):
        method_name = methods[choice]
        
        # If the method is get_token_pool_stat, prompt for pool address
        if method_name == "get_token_pool_stat":
            pool_address = input("Enter the pool address: ")
            result = getattr(token_obj, method_name)(pool_address)
        else:
            result = getattr(token_obj, method_name)()
        
        print(f"\nResult of {method_name}:")
        print_json(result)
    else:
        print("Invalid choice.")

def wallet_attr():
    # Ask user for wallet address
    wallet_address = input("Enter the wallet address: ")

    # Create an instance of Wallet
    wallet_obj = Wallet(wallet_address)

    # Get all methods of the object excluding private ones
    methods = [method for method in dir(wallet_obj) if callable(getattr(wallet_obj, method)) and not method.startswith("_")]

    # Display the methods
    print("\nAvailable methods:")
    for i, method in enumerate(methods, 1):
        print(f"{i}. {method}")

    # Ask the user to choose a method
    choice = int(input("\nEnter the number of the method you want to call: ")) - 1

    # Call the selected method
    if 0 <= choice < len(methods):
        method_name = methods[choice]
        
        # If the method is get_token_pnl_data, prompt for token address
        if method_name == "get_token_pnl_data":
            token_address = input("Enter the token address: ")
            result = getattr(wallet_obj, method_name)(token_address)
        else:
            result = getattr(wallet_obj, method_name)()

        print(f"\nResult of {method_name}:")
        print_json(result)
    else:
        print("Invalid choice.")


while True:
    print("\n Test Script")
    choice = input("1. Token Functions   2. Wallet Functions    3. End\n")

    if choice == "1":
        token_attr()
    elif choice == '2':
        wallet_attr()
    elif choice =='3':
        break
    else:
        print("Invalid Input")