import json
with open("euro.json", "r") as file:
    data = json.load(file)
rates = data["rates"]
print("Date            Buying Rate     Selling Rate")
print("============================================")
for i in range(len(rates)-1):
    print(rates[i]["effectiveDate"]," "*6,rates[i]["bid"], " "*10, rates[i]["ask"]," ")