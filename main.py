# Tip calculator

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
tip_amount = bill * tip_as_percent
total_bill = bill + tip_amount
split_bill = round(total_bill / num_people, 2)
split_bill = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${split_bill}")
