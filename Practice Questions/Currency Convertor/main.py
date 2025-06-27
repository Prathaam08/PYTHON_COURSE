with open('Practice Questions/Currency Convertor/currencyRate.txt') as f:
    lines = f.readlines()

currencyDict ={}

indAmount = int(input("Enter the amount you want to convert: "))

for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

 
[print(item) for item in currencyDict.keys()]

print("copy and paste the country name you want to convert your currency")
foriegncurency = input("Enter the name : ")
print(f"{indAmount} INR is equal to {indAmount * float(currencyDict[foriegncurency])} {foriegncurency}")

