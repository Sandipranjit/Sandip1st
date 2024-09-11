import random

dice = int(input("How many dices you want to roll? "))
dice_sum = 0

for i in range(dice):
    roll = random.randint(1,6)
    dice_sum += roll
print(f"The sum of the rolled dices is: {dice_sum}")
