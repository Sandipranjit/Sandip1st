names = set()

while True:
    name = input("Enter your name or press Enter to finish: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
        
print("\nList of names: ")
for name in names:
    print("- ", name)

