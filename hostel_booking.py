print("----- Welcome to Hotel Booking System -----")

# Guest Details
name = input("Enter guest name: ")
age = int(input("Enter age: "))
gender = input("Enter gender (M/F/O): ")
mobile = input("Enter mobile number: ")
email = input("Enter email: ")

# Room Type Selection
print("\nRoom Type:")
print("1. Standard Room  - ₹2000 per night")
print("2. Deluxe Room  - ₹4000 per night")
print("3. Suite Room   - ₹7000 per night")
room_choice = int(input("Choose room (1/2/3): "))

if room_choice == 1:
    room_cost = 2000
    room_name = "Standard Room"
elif room_choice == 2:
    room_cost = 4000
    room_name = "Deluxe Room"
elif room_choice == 3:
    room_cost = 7000
    room_name = "Suite Room"
else:
    print("Invalid choice! Default room selected: Standard Room")
    room_cost = 2000
    room_name = "Standard Room"

# Optional Services
breakfast = input("Do you want complimentary breakfast? (yes/no): ").lower()
spa = input("Do you want spa access? (yes/no): ").lower()
parking = input("Do you want parking? (yes/no): ").lower()

breakfast_cost = 500 if breakfast == "yes" else 0
spa_cost = 1500 if spa == "yes" else 0
parking_cost = 300 if parking == "yes" else 0

# Meal Plan
meal_plan = input("Meal plan (all-inclusive / breakfast-only / none): ").lower()
if meal_plan == "all-inclusive":
    meal_cost = 2000
elif meal_plan == "breakfast-only":
    meal_cost = 500
else:
    meal_cost = 0

# Number of Nights
nights = int(input("Enter number of nights: "))

# Total Cost Calculation
total = (room_cost * nights) + breakfast_cost + spa_cost + parking_cost + meal_cost

# Final Output
print("\n----- BOOKING SUMMARY -----")
print("Guest Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Mobile:", mobile)
print("Email:", email)
print("Room Selected:", room_name)
print("Room Cost per Night: ₹", room_cost)
print("Breakfast Charges: ₹", breakfast_cost)
print("Spa Access: ₹", spa_cost)
print("Parking Charges: ₹", parking_cost)
print("Meal Plan:", meal_plan.title())
print("Meal Plan Cost: ₹", meal_cost)
print("Total Nights:", nights)
print("\nTotal Amount to Pay: ₹", total)
print("-------------------------------------")
print("Thank you for booking with us!")
print("Check-in time: 2:00 PM | Check-out time: 11:00 AM")