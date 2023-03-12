print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people are splitting the bill?"))
percentage = (tip/100) + 1
total = (total_bill) * (percentage) / (people)
money = format(float(total), ".2f")
print(f"Each person should pay: £{money}")