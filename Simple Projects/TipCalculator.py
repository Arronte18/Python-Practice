# simple tip calculator using arithmetic operators

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tipPercentage = tip / 100
payment = round(((bill * tipPercentage) + bill) / people, 2)

print(f"You have to pay: {payment}")