from coinbase.wallet.client import Client

api_key = ''
api_secret = ''

targetPaymentMethod = "EUR Wallet"
targetBuyCurrencyWallet = "BAT Wallet"
targetCurrency = "BAT"
targetAmountToBuy = "23.64"

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
print(buy["total"]["amount"])

