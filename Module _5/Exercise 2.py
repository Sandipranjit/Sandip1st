number = []

user_input = input("Enter a number or press Enter to quit: ")

while user_input != "":
    number.append(int(user_input))
    user_input = input("Enter another number or press Enter to quit: ")

number.sort(reverse=True)
print(number[:5])






