gender=input("Please, enter your preferred gender(female or male): ").lower()
hemoglobin=float(input("And, your hemoglobin value(g/l): "))
if gender=="female":
    if 117 <=hemoglobin <=155:
        print("Your hemoglobin value is normal.")
    elif hemoglobin <117:
        print("Your hemoglobin value is low.")
    else:
        print("Your hemoglobin value is high.")
elif gender=="male":
    if 134 <= hemoglobin <=167:
        print("Your hemoglobin value is normal.")
    elif hemoglobin <134:
        print("Your hemoglobin value is low.")
    else:
        print("Your hemoglobin value is high.")







