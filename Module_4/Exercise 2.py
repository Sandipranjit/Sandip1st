number = float(input("Please, enter a positive number(inch): "))

while number > 0:
    print(f"After conversion in centimeters, the value will be {number*2.54: .2f} cm.")
    number = float(input("Please, enter a positive number again(inch): "))

print("Invalid input! The program ends here.")
