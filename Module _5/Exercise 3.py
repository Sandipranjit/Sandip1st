number = int(input("Enter a number: "))
divider = 0

for i in range(1, number + 1):

    if number % i == 0:
        divider += 1

if divider == 2:
    print("The number is prime.")

else:
    print("The number is not prime.")

