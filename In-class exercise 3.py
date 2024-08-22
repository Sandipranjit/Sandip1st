# first calculation
times = float(input("How many times do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
expenditure = float(input("How much money do you spend on groceries in a week?"))
print("Average food expenditure:")
print("Daily: " f"{(times*price+expenditure)/7} euros")
print("Weekly: " f"{times*price+expenditure} euros")

# second calculation
times = float(input("How many times do you eat at the student cafeteria?"))
price = float(input("The price os a typical student lunch?"))
expenditure = float(input("How much money do you spend on groceries in a week?"))
weekly = (times*price+expenditure)
daily = (weekly/7)
print("Average food expenditure:")
print("Daily: " f"{daily} euros")
print("Weekly: " f"{weekly} euros")





