from random import uniform

N = int(input("Enter how many points to generate?: "))
n = 0

loop = N
while loop > 0:
    X = uniform(-1,1)
    Y = uniform(-1,1)
    if X**2+Y**2<1:
        n +=1
    loop -=1

print("Approximate pi: = ", (4*n)/N)

