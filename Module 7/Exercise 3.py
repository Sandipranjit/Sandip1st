airport_data = {}

while True:
    print("You have the following options:")
    print("1. Enter a new airport.")
    print("2. Fetch information of an existing airport.")
    print("3. Quit.")

    choice = input("\nEnter your choice from the options above: ")
    if choice == "1":
        icao_code = input("\nEnter ICAO code of the new airport: ")
        name_airport = input("Enter name of the airport: ")
        airport_data[icao_code] = name_airport
        print(f"Airport {name_airport} with ICAO code {icao_code} has been added.")

    elif choice == "2":
        icao_code = input("\nEnter ICAO code of the airport to fetch: ")
        if icao_code in airport_data:
            print(f"Airport with ICAO code '{icao_code}' is '{airport_data[icao_code]}'.")
        else:
            print("Airport with the ICAO code not found.")

    elif choice == "3":
        print("Quitting....Goodbye!")
        break

else:
    print("Invalid option. Please choose from options 1, 2 or 3  from above.")