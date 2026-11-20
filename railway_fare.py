
# railway_fare.py

distance = float(input("Enter journey distance in km: "))
travel_class = input("Enter travel class (SL, 3A or 2A): ")

if travel_class == "SL":
    fare = distance * 0.80
    print("Travel Class: SL")
    print("Total Fare: ₹" + str(fare))

elif travel_class == "3A":
    fare = distance * 2.10
    print("Travel Class: 3A")
    print("Total Fare: ₹" + str(fare))

elif travel_class == "2A":
    fare = distance * 3.00
    print("Travel Class: 2A")
    print("Total Fare: ₹" + str(fare))

else:
    print("Invalid travel class!")
