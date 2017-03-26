import poloniex
import requests 
import json

APIKeySecret = open("poloAPI.txt").read().strip().split()
APIKey = APIKeySecret[0]
APISecret = APIKeySecret[1]
polo = poloniex.Poloniex(APIKey, APISecret)
loans = polo.returnActiveLoans()["provided"]

btcPrice = json.loads(requests.get("https://api.btcmarkets.net/market/BTC/AUD/tick").content.decode("utf-8"))["lastPrice"]
finalFees = 0
currentAmount = 0
currentFees = 0
totalDays = 0

for loan in loans:
    currentFees += float(loan["fees"])
    currentAmount += float(loan["amount"])
    finalFees += float(loan["rate"]) * float(loan["amount"]) * int(loan["duration"])
    totalDays += int(loan["duration"])
    
    

finalFeesBTC = str(finalFees)
finalFeesAUD = str(finalFees * btcPrice)

finalBalanceBTC = str(finalFees + currentAmount)
finalBalanceAUD = str((finalFees + currentAmount) * btcPrice)

currentBalanceBTC = str(currentFees + currentAmount)
currentBalanceAUD = str((currentFees + currentAmount) * btcPrice)

unPayedFeesBTC = str(finalFees - currentFees)
unPayedFeesAUD = str((finalFees - currentFees) * btcPrice)

percentFeesPayed = str(round(currentFees/(finalFees/100), 2))

feesPerDayBTC = str(finalFees / totalDays * len(loans))
feesPerDayAUD = str(finalFees / totalDays * len(loans) * btcPrice)

print("Final fees \n\tBTC: " + finalFeesBTC + "\n\tAUD: " + finalFeesAUD + "\n")
print("Final Balance \n\tBTC: " + finalBalanceBTC + "\n\tAUD: " + finalBalanceAUD + "\n")
print("Current balance \n\tBTC: " + currentBalanceBTC + "\n\tAUD: " + currentBalanceAUD + "\n")
print("Unpayed fees \n\tBTC: " + unPayedFeesBTC + "\n\tAUD: " + unPayedFeesAUD + "\n")
print("Percent of fees payed \n\tPercent: " + percentFeesPayed + "%\n")
print("Fees per day \n\tBTC: " + feesPerDayBTC + "\n\tAUD: " + feesPerDayAUD + "\n")



