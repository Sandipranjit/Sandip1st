import random

def dice(num_sides):
    return random.randint(1, num_sides)

num_sides = int(input("Enter number of sides of your choice on the dice = "))

while True:
    number = dice(num_sides)
    print(f"The results of each roll = {number}")

    if number == num_sides:
        break

