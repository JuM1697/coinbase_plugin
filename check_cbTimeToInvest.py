#!/usr/bin/python3
import sys, argparse
from coinbase.wallet.client import Client

parser = argparse.ArgumentParser(description='Get the current Price of Coinbase Cryptos')
parser.add_argument("-k", "--key", required=True, help="Coinbase API Key")
parser.add_argument("-s", "--secret", required=True, help="Coinbase API Secret")
parser.add_argument("-p", "--paymentMethod", required=True, help="Desired Target Payment Method e.g. EUR Wallet")
parser.add_argument("-c", "--currencyToBuy", required=True, help="Desired Target Currency to buy e.g. BTC")
parser.add_argument("-a", "--accountWallet", required=True, help="Desired Target wallet to buy from e.g. BAT Wallet")
parser.add_argument("-i", "--invest", required=True, help="Desired amount to invest from Payment Method e.g. 5.00")
parser.add_argument("-b", "--buy", required=True, help="How much of the desired Crypto would you like to buy for the previously defined amount to invest? e.g. 23")
args = vars(parser.parse_args())


api_key = args["key"]
api_secret = args["secret"]
targetPaymentMethod = args["paymentMethod"]
targetCurrency = args["currencyToBuy"]
targetBuyCurrencyWallet = args["accountWallet"]
investMoney = args["invest"]
targetAmountToBuy = args["buy"]



client = Client(api_key, api_secret)
accounts = client.get_accounts()
pms = client.get_payment_methods()

for method in pms.data:
    if method['name'] == targetPaymentMethod:
        paymentID = method['id']


for account in accounts.data:
    if account['name'] == targetBuyCurrencyWallet:
        accountID = account['id']


buy = client.buy(accountID,commit="false",amount=targetAmountToBuy, currency=targetCurrency, payment_method=paymentID, quote="true")

costs = buy["total"]["amount"]

if costs < investMoney:
    print("Your desired target price is reached! | price="+costs)
    sys.exit(2)
else:
    print("Your desired target price is not reached. Keep waiting! | price="+costs)
    sys.exit(0)
