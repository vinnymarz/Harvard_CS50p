import requests
import sys

def get_bitcoin_price():
    try:
        input_amount = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    conversion = response.json()
    rate = conversion["bpi"]["USD"]["rate_float"]
    converted_amount = input_amount * rate
    print(f"${converted_amount:,.4f}")

get_bitcoin_price()
