import requests

KEY = "" #PUT YOUR API KEY HERE


#HANDLES THE REQUESTS
def handle_request(token_details:requests):
    if token_details.status_code == 200:
        try:
            response_json = token_details.json()
            return response_json
        except ValueError:
            print("Failed to decode JSON from the response.")
    else:
        print(f"Request failed with status code {token_details.status_code}: {token_details.text}")
    pass


#HANDLES JSON DISPLAY
def print_json(data, indent=0):
    if data:
        try:
            for key, value in data.items():
                if isinstance(value, dict):
                    print("    " * indent + f"{key}:")
                    print_json(value, indent + 1)
                elif isinstance(value, list):
                    print("    " * indent + f"{key}:")
                    for item in value:
                        print_json(item, indent + 1)
                else:
                    print("    " * indent + f"{key}: {value}")
        except Exception as e:
            print(f"{e}")
    else:
        print("No data returned")