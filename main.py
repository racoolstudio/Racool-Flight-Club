# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from data_manager import *
#
from notification_manager import *
from data_manager import *

# Create an instance of the DataManager class.
flight = DataManager()

# Welcome message for Racool's Flight Club.
print('Welcome to Racool\'s Flight Club ✈️')

# Prompt the user to enter their details.
first_name = input('Enter Your First Name: ')
last_name = input('Enter Your Last Name: ')
email = input('Enter Your Email: ')

# Create a new user using the entered details.
flight.create_user(first_name, last_name, email)

# Get the list of flights with the lowest prices.
flight_list = flight.check_for_lowest_price()

# Initialize variables to handle errors.
isError = False
error_message = ''

# Iterate through the list of flights and notify users of available deals.
for flight_info in flight_list:
    try:
        # Send notifications to all users' emails.
        for email in flight.users_email():
            NotificationManager(
                flight_info['city'], flight_info['price'], flight_info['departure_city_name'],
                flight_info['departure_airport_code'],
                flight_info['arrival_city_name'],
                flight_info['arrival_airport_code'],
                flight_info['available_seats'],
                flight_info['number_of_days'],
                flight_info['outbound_date'],
                flight_info['inbound_date'],
                flight_info['link']
            ).send_message(email)
    except TypeError:
        # Handle any errors and update the error_message variable.
        isError = True
        error_message += flight_info

# If there are errors, send an error message to all users' emails.
if isError:
    for email in flight.users_email():
        NotificationManager('', '', '', '', '', '', '', '', '', '', '').error_message(email, error_message)
