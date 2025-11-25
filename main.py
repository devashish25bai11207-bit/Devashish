# ============================================
# HOTEL BOOKING MANAGEMENT SYSTEM
# ============================================
# This program allows guests to book hotel rooms
# with various amenities and services
# ============================================

def print_header():
    """Display the welcome header"""
    print("=" * 50)
    print("----- Welcome to Hotel Booking System -----")
    print("=" * 50)
    print()

def get_guest_name():
    """Get guest name from user"""
    name = input("Enter guest name: ")
    return name

def get_guest_age():
    """Get guest age from user"""
    age = int(input("Enter age: "))
    return age

def get_guest_gender():
    """Get guest gender from user"""
    gender = input("Enter gender (M/F/O): ")
    return gender

def get_guest_mobile():
    """Get guest mobile number from user"""
    mobile = input("Enter mobile number: ")
    return mobile

def get_guest_email():
    """Get guest email from user"""
    email = input("Enter email: ")
    return email

def display_room_menu():
    """Display available room types and prices"""
    print("\n" + "=" * 50)
    print("ROOM TYPE SELECTION")
    print("=" * 50)
    print("1. Standard Room  - ₹2000 per night")
    print("2. Deluxe Room    - ₹4000 per night")
    print("3. Suite Room     - ₹7000 per night")
    print("=" * 50)

def get_room_choice():
    """Get room choice from user"""
    room_choice = int(input("Choose room (1/2/3): "))
    return room_choice

def process_room_selection(room_choice):
    """Process room selection and return cost and name"""
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
    return room_cost, room_name

def display_services_header():
    """Display header for optional services"""
    print("\n" + "=" * 50)
    print("OPTIONAL SERVICES")
    print("=" * 50)

def get_breakfast_choice():
    """Get breakfast service choice"""
    breakfast = input("Do you want complimentary breakfast? (yes/no): ").lower()
    return breakfast

def get_spa_choice():
    """Get spa service choice"""
    spa = input("Do you want spa access? (yes/no): ").lower()
    return spa

def get_parking_choice():
    """Get parking service choice"""
    parking = input("Do you want parking? (yes/no): ").lower()
    return parking

def calculate_breakfast_cost(breakfast):
    """Calculate breakfast cost"""
    breakfast_cost = 500 if breakfast == "yes" else 0
    return breakfast_cost

def calculate_spa_cost(spa):
    """Calculate spa cost"""
    spa_cost = 1500 if spa == "yes" else 0
    return spa_cost

def calculate_parking_cost(parking):
    """Calculate parking cost"""
    parking_cost = 300 if parking == "yes" else 0
    return parking_cost

def display_meal_plan_header():
    """Display meal plan header"""
    print("\n" + "=" * 50)
    print("MEAL PLAN OPTIONS")
    print("=" * 50)

def get_meal_plan():
    """Get meal plan choice"""
    meal_plan = input("Meal plan (all-inclusive / breakfast-only / none): ").lower()
    return meal_plan

def calculate_meal_cost(meal_plan):
    """Calculate meal plan cost"""
    if meal_plan == "all-inclusive":
        meal_cost = 2000
    elif meal_plan == "breakfast-only":
        meal_cost = 500
    else:
        meal_cost = 0
    return meal_cost

def get_number_of_nights():
    """Get number of nights for stay"""
    print("\n" + "=" * 50)
    nights = int(input("Enter number of nights: "))
    return nights

def calculate_total_cost(room_cost, nights, breakfast_cost, spa_cost, parking_cost, meal_cost):
    """Calculate total booking cost"""
    total = (room_cost * nights) + breakfast_cost + spa_cost + parking_cost + meal_cost
    return total

def print_booking_summary_header():
    """Print booking summary header"""
    print("\n" + "=" * 50)
    print("----- BOOKING SUMMARY -----")
    print("=" * 50)

def print_guest_details(name, age, gender, mobile, email):
    """Print guest details in summary"""
    print("Guest Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Mobile:", mobile)
    print("Email:", email)
    print("-" * 50)

def print_room_details(room_name, room_cost):
    """Print room details in summary"""
    print("Room Selected:", room_name)
    print("Room Cost per Night: ₹", room_cost)

def print_service_charges(breakfast_cost, spa_cost, parking_cost):
    """Print service charges in summary"""
    print("Breakfast Charges: ₹", breakfast_cost)
    print("Spa Access: ₹", spa_cost)
    print("Parking Charges: ₹", parking_cost)

def print_meal_details(meal_plan, meal_cost):
    """Print meal plan details"""
    print("Meal Plan:", meal_plan.title())
    print("Meal Plan Cost: ₹", meal_cost)

def print_stay_details(nights):
    """Print stay duration details"""
    print("Total Nights:", nights)
    print("-" * 50)

def print_total_amount(total):
    """Print total amount to pay"""
    print("\nTotal Amount to Pay: ₹", total)
    print("=" * 50)

def print_footer():
    """Print thank you message and hotel policies"""
    print("Thank you for booking with us!")
    print("Check-in time: 2:00 PM | Check-out time: 11:00 AM")
    print("=" * 50)

# ============================================
# MAIN PROGRAM EXECUTION
# ============================================

# Display welcome header
print_header()

# Collect guest details
name = get_guest_name()
age = get_guest_age()
gender = get_guest_gender()
mobile = get_guest_mobile()
email = get_guest_email()

# Room selection process
display_room_menu()
room_choice = get_room_choice()
room_cost, room_name = process_room_selection(room_choice)

# Optional services selection
display_services_header()
breakfast = get_breakfast_choice()
spa = get_spa_choice()
parking = get_parking_choice()

# Calculate service costs
breakfast_cost = calculate_breakfast_cost(breakfast)
spa_cost = calculate_spa_cost(spa)
parking_cost = calculate_parking_cost(parking)

# Meal plan selection
display_meal_plan_header()
meal_plan = get_meal_plan()
meal_cost = calculate_meal_cost(meal_plan)

# Get stay duration
nights = get_number_of_nights()

# Calculate total cost
total = calculate_total_cost(room_cost, nights, breakfast_cost, spa_cost, parking_cost, meal_cost)

# Display booking summary
print_booking_summary_header()
print_guest_details(name, age, gender, mobile, email)
print_room_details(room_name, room_cost)
print_service_charges(breakfast_cost, spa_cost, parking_cost)
print_meal_details(meal_plan, meal_cost)
print_stay_details(nights)
print_total_amount(total)
print_footer()
