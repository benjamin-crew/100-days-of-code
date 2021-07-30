total_bill = float(input("What was the total bill?: $"))
tip = (float(input("What percentage tip would you like to give?: "))) / 100 + 1

people = int(input("How many people are splitting?: "))

price_per_person = "{:.2f}".format(round(total_bill / people * tip, 2))

print(f"Each person should pay: {price_per_person}")