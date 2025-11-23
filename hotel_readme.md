# Hotel Booking System

A simple command-line based hotel booking and billing system built with Python.

## Features

- **Guest Registration**: Collect guest details including name, age, gender, mobile, and email
- **Room Selection**: Choose from 3 room types with different pricing
  - Standard Room - ₹2000 per night
  - Deluxe Room - ₹4000 per night
  - Suite Room - ₹7000 per night
- **Optional Services**:
  - Complimentary Breakfast (₹500)
  - Spa Access (₹1500)
  - Parking (₹300)
- **Meal Plans**:
  - All-Inclusive (₹2000)
  - Breakfast-Only (₹500)
  - None
- **Automatic Bill Generation**: Calculates total cost based on room, services, and duration

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Ensure Python 3 is installed on your system

## Usage

Run the program using:

```bash
python hotel_booking.py
```

Follow the on-screen prompts to:
1. Enter guest details
2. Select room type
3. Choose optional services
4. Select meal plan
5. Enter number of nights
6. View the final booking summary and bill

## Example Output

```
----- Welcome to Hotel Booking System -----
Enter guest name: John Doe
Enter age: 30
Enter gender (M/F/O): M
Enter mobile number: 9876543210
Enter email: john@example.com

Room Type:
1. Standard Room  - ₹2000 per night
2. Deluxe Room  - ₹4000 per night
3. Suite Room   - ₹7000 per night
Choose room (1/2/3): 2

Do you want complimentary breakfast? (yes/no): yes
Do you want spa access? (yes/no): no
Do you want parking? (yes/no): yes
Meal plan (all-inclusive / breakfast-only / none): breakfast-only
Enter number of nights: 3

----- BOOKING SUMMARY -----
Guest Name: John Doe
Age: 30
Gender: M
Mobile: 9876543210
Email: john@example.com
Room Selected: Deluxe Room
Room Cost per Night: ₹ 4000
Breakfast Charges: ₹ 500
Spa Access: ₹ 0
Parking Charges: ₹ 300
Meal Plan: Breakfast-Only
Meal Plan Cost: ₹ 500
Total Nights: 3

Total Amount to Pay: ₹ 13300
-------------------------------------
Thank you for booking with us!
Check-in time: 2:00 PM | Check-out time: 11:00 AM
```

## Future Enhancements

- Input validation for all fields
- Date-based booking system
- Payment gateway integration
- Discount codes and offers
- Database integration for storing bookings
- GUI interface
- Receipt generation (PDF)
- Booking confirmation via email/SMS

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.