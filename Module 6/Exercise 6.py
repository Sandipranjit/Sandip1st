import math

def pizza(diameter_cm, price_euro):

    diameter_m = diameter_cm * 0.01
    area_m2 = math.pi * (diameter_m**2)
    price = price_euro /area_m2
    return price

diameter1= float(input("Enter the diameter of mozzarella pizza(cm): "))
mozzarella =  float(input("Enter the price of mozzarella pizza(€): "))

diameter2 = float(input("\nEnter the diameter of porcine pizza(cm): "))
porcine = float(input("Enter the price of porcine pizza(€): "))

unit_price1 = pizza(diameter1, mozzarella)
print(f"\nThe unit price of mozzarella pizza: {unit_price1:.2f} per square meter.")

unit_price2 = pizza(diameter2, porcine)
print(f"The unit price of porcine pizza: {unit_price2:.2f} per square meter.")

if unit_price1 < unit_price2:
    print("\nThe mozzarella pizza provides better value than porcine pizza.")
elif unit_price1 > unit_price2:
    print("\n>=The porcine pizza provides better value than mozzarella pizza.")
else:
    print("Both pizza have the same price.")


