# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# from data_manager import *
#
from notification_manager import *
from data_manager import *

flight = DataManager()

# print('Welcome to Racool\'s Flight Club ✈️')
# first_name = input('Enter Your First Name : ')
# last_name = input('Enter Your Last Name : ')
# email = input('Enter Your Email : ')
# flight.create_user(first_name,last_name,email)
flight_list = flight.check_for_lowest_price()
isError = False
error_message = ''
for flight_info in flight_list:
    try:
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
            ).send_message(email),
    except TypeError:
        isError = True
        error_message += flight_info

if isError:
    for email in flight.users_email():
        NotificationManager('', '', '', '', '', '', '', '', '',
                            '', '').error_message(email, error_message)
