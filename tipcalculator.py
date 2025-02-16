print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_people = int(input("How many people to split the bill? "))

tip_as_percent = percentage_tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
result = total_bill / split_people

# result = (total_bill / split_people) * ((100 + percentage_tip)*0.01)
# print(f"Each person should pay: ${round(result, 2)}")
print(f"Each person should pay: ${"{:.2f}".format(result)}")