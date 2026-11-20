distance = float(input("Enter journey distance in km: "))
travel_class = input("Enter travel class (SL, 3A or 2A): ")
age = int(input("Enter passenger age: "))

if travel_class == "SL":
    base_fare = distance * 0.80

    if age >= 60:
        concession = base_fare * 40 / 100
    elif age < 12:
        concession = base_fare * 50 / 100
    else:
        concession = 0

    final_fare = base_fare - concession

elif travel_class == "3A":
    base_fare = distance * 2.10
    concession = 0
    final_fare = base_fare

elif travel_class == "2A":
    base_fare = distance * 3.00
    concession = 0
    final_fare = base_fare

else:
    print("Invalid travel class!")
    base_fare = 0
    concession = 0
    final_fare = 0

if travel_class == "SL" or travel_class == "3A" or travel_class == "2A":
    print("\nBase Fare: ₹" + str(base_fare))
    print("Concession Amount: ₹" + str(concession))
    print("Final Fare: ₹" + str(final_fare))
