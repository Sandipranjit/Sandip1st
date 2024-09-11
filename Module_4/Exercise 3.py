largest = 0
smallest = 0

number = input("Enter a number or press Enter to quit: ")

if number != "":
    largest = float(number)
    smallest = float(number)

while number != "":
    if float(number) >= largest:
        largest = float(number)

    if float(number) <= smallest:
        smallest = float(number)

    number = input("Enter another number or press Enter to quit: ")

print("The largest number is: " + str(largest))
print("The smallest number is: " + str(smallest))










