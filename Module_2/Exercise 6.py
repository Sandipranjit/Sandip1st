import random

def generate_3_digit():
    #generating random combination of 3-digit code between 0 and 9
    combination=[random.randint(0,9) for _ in range(3)]
    return combination

combinationA=generate_3_digit()
print(f"The random 3-digit code is: {combinationA}")

def generate_4_digit():
    #generating random combination of 4-digit code between 1 and 6
    combination=[random.randint(1,6) for _ in range(4)]
    return combination

combinationB=generate_4_digit()
print(f"The random 4-digit code is: {combinationB}")
