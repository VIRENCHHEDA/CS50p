import sys
import requests

if len(sys.argv) == 2:            #checking for 2 command line arguments
    try:
        bitcoin = float(sys.argv[1])     #bitcoin input should only be a number
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")       #checking for no command line argument
    sys.exit(1)

#using get func for API , .json for api in library format
try:
    btc_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
    print(f"${bitcoin * btc_price:,.4f}")          #:,.4f is used for 4 decimal places

except requests.RequestException:
    sys.exit(1)