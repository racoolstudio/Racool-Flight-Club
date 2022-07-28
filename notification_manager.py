import os
from smtplib import SMTP

my_gmail = os.getenv('USERNAME') # use your email address
my_gmail_password = os.getenv('PASSWORD') # your email password


class NotificationManager:
    def __init__(self, city, price, departure_city_name, departure_airport_code, arrival_city_name,
                 arrival_airport_code, available_seats, number_of_days, outbound_date, inbound_date, link):
        self.city = city
        self.price = price
        self.departure_city_name = departure_city_name
        self.departure_airport_code = departure_airport_code
        self.arrival_city_name = arrival_city_name
        self.arrival_airport_code = arrival_airport_code
        self.available_seats = available_seats
        self.number_of_days = number_of_days
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.link = link

    def send_message(self,email):

        with SMTP('smtp.gmail.com') as sending:
            sending.starttls()
            sending.login(user=my_gmail, password=my_gmail_password)
            sending.sendmail(from_addr=my_gmail, to_addrs=email,
                             msg=f'Subject:Cheap Flight Alert!\n\n'
                                 f'\nTravelling to {self.city} costs only {self.price} CAD 🥳!'
                                 f'\nDeparture City Name : {self.departure_city_name}'
                                 f'\nDeparture Airport Code:{self.departure_airport_code}'
                                 f'\nArrival City Name : {self.arrival_city_name}'
                                 f'\nArrival Airport Code : {self.arrival_airport_code}'
                                 f'\nAvailable seats : {self.available_seats}'
                                 f'\nLength of Stay: {self.number_of_days} Nights'
                                 f'\nOutbound Date : {self.outbound_date}'
                                 f'\nInbound Date : {self.inbound_date}'
                                 f'\nBook Here : {self.link}',
                             )

    def error_message(self,email,message):
        with SMTP('smtp.gmail.com') as sending:
            sending.starttls()
            sending.login(user=my_gmail, password=my_gmail_password)
            sending.sendmail(from_addr=my_gmail, to_addrs=email,
                             msg=f'Subject:Cheap Flight Alert!\n\n{message}')