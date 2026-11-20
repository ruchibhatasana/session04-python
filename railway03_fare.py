
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


    print("\n================================")
    print("       RUCHI RAILWAY TICKET")
    print("================================")
    print("Travel Class:\t" + travel_class)
    print("Distance:\t" + str(distance) + " km")
    print("Passenger Age:\t" + str(age))
    print("--------------------------------")
    print("Base Fare:\t₹" + str(base_fare))
    print("Concession:\t₹" + str(concession))
    print("--------------------------------")
    print("Final Fare:\t₹" + str(final_fare))
    print("================================")
    print("       HAPPY JOURNEY!")
    print("================================")


# =====================================
# TEST CASE 1
# Input:
# Travel Class: SL
# Distance: 250 km
# Age: 65
#
# Output:
# RUCHI RAILWAY TICKET
# Travel Class: SL
# Distance: 250.0 km
# Passenger Age: 65
# Base Fare: ₹200.0
# Concession: ₹80.0
# Final Fare: ₹120.0
# HAPPY JOURNEY!
#
#
# =====================================
# TEST CASE 2
# Input:
# Travel Class: SL
# Distance: 100 km
# Age: 8
#
# Output:
# RUCHI RAILWAY TICKET
# Travel Class: SL
# Distance: 100.0 km
# Passenger Age: 8
# Base Fare: ₹80.0
# Concession: ₹40.0
# Final Fare: ₹40.0
# HAPPY JOURNEY!
#
#
# =====================================
# TEST CASE 3
# Input:
# Travel Class: 3A
# Distance: 400 km
# Age: 35
#
# Output:
# RUCHI RAILWAY TICKET
# Travel Class: 3A
# Distance: 400.0 km
# Passenger Age: 35
# Base Fare: ₹840.0
# Concession: ₹0
# Final Fare: ₹840.0
# HAPPY JOURNEY!
#
#
# =====================================
# TEST CASE 4
# Input:
# Travel Class: 2A
# Distance: -50 km
# Age: 30
#
# Output:
# Error: Distance must be greater than zero.
#
#
# =====================================
# TEST CASE 5
# Input:
# Travel Class: AC
# Distance: 200 km
# Age: 40
#
# Output:
# Error: Invalid travel class!
