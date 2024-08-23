print("Enter mass in medieval units below: ")
talents=float(input("Enter the number of talents: "))
pounds=float(input("Enter the number of pounds: "))
lots=float(input("Enter the number of lots: "))

#if 1 lot is 13.3gms, then 1 pound is 425.6gms or 32 lots
#if 1 pound is 425.6 gms, then 1 talent is 8.5gms or 20 pound

lots_gms=13.3
pounds_to_lots=32
talents_to_pounds=20

#converting all units to lots and then to grams
lots_total=(talents_to_pounds*pounds_to_lots*talents)+(pounds_to_lots*pounds)+lots
total_lots_gms=lots_total*lots_gms

#converting grams to kg and gms
total_kg=float(total_lots_gms//1000)
gms=total_lots_gms%1000

#Finally
print("The weight in modern units: ")
print(f"{total_kg:.2f} kilograms and {gms:.2f} grams.")



