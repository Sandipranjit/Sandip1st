attempt = 5

while attempt > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "python" and password == "rules":
        print("Welcome!")
        break

    if username != "python" and password != "rules":
        attempt -= 1
        if attempt == 0:
            print("Access denied!!!")
            break

    print("Correct your username and password!")
