import random

def dice():
    return random.randint(1,6)

while True:

    roll = dice()
    print(f"The results of each roll = {roll}")

    if roll == 6:
        break


