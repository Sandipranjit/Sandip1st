print("Please, provide 3 integer numbers of your choice.")
one=int(input("First number: "))
second=int(input("Second number: "))
third=int(input("Third number: "))
print("Breaking down your results as follows: ")
sum=one+second+third
product=one*second*third
average=sum/3
print("The sum of your numbers is: " + str(sum))
print("The product of your numbers is: " + str(product))
print(f"The average of your numbers is: {average:.2f}")