
distance = float(input("Enter journey distance in km: "))
travel_class = input("Enter travel class (SL, 3A or 2A): ")
age = int(input("Enter passenger age: "))

if distance <= 0:
    print("Error: Distance must be greater than zero.")

elif distance > 3000:
    print("Error: Distance cannot exceed 3000 km.")

elif age < 1 or age > 120:
    print("Error: Age must be between 1 and 120.")

elif travel_class != "SL" and travel_class != "3A" and travel_class != "2A":
    print("Error: Invalid travel class!")

else:

    if travel_class == "SL":
        base_fare = distance * 0.80


        if age >= 60:
            concession = base_fare * 40 / 100

        elif age < 12:
            concession = base_fare * 50 / 100

        else:
            concession = 0

    elif travel_class == "3A":
        base_fare = distance * 2.10
        concession = 0

    else:
        base_fare = distance * 3.00
        concession = 0

    final_fare = base_fare - concession

    print("\n----- Railway Fare Details -----")
    print("Travel Class:\t" + travel_class)
    print("Distance:\t" + str(distance) + " km")
    print("Passenger Age:\t" + str(age))
    print("Base Fare:\t₹" + str(base_fare))
    print("Concession:\t₹" + str(concession))
    print("Final Fare:\t₹" + str(final_fare))
