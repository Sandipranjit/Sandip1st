def conv(gasoline):

    to_litres = float(gasoline * 3.78541)
    return to_litres

while True:
    gasoline = float(input("Enter the volume of gasoline in American gallons = "))

    if gasoline < 1:
        break

    to_litres = conv(gasoline)
    print(f"The conversion of gallons to litres is = {to_litres:.2f} litres.")






