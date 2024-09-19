def get_season(month_number):
    seasons = ("Winter", "Spring", "Summer", "Autumn")

    if month_number in (12,1,2):
        place_index = 0
    elif month_number in (3,4,5):
        place_index = 1
    elif month_number in (6,7,8):
        place_index = 2
    elif month_number in (9,10,11):
        place_index = 3
    else:
        print("Invalid month number!!!")
    return seasons[place_index]

month_number = int(input("Enter month's number only between 1 and 12: "))

print(f"The month falls in {get_season(month_number)} season.")