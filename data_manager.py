from flight_data import *
from flight_data import FlightData
from flight_search import *

sheety_api = os.getenv('SHEETYAPI')
sheety_endpoint = 'https://api.sheety.co/3de9979c4873c471b7d88611ef649ffc/flight'
headers = {
    'Authorization': sheety_api
}


class DataManager:
    def __init__(self):
        self.flights_data = get(url=f'{sheety_endpoint}/prices', headers=headers).json()
        self.users_data = get(url=f'{sheety_endpoint}/users', headers=headers).json()

    def users_email(self):
        email = [i['email'] for i in self.users_data['users']]
        return email

    def create_user(self, first_name, last_name, email):
        confirm_email = input('Kindly type your email again for confirmation : ')
        new_user = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        if confirm_email == email:
            print(f'Welcome to the flight club {first_name}')
            post(url=f'{sheety_endpoint}/users', json=new_user, headers=headers)
        else:
            print('Oops!!! 😂 kindly try again.')
            self.create_user(first_name, last_name, email)

    def check_for_lowest_price(self):

        cheapest = []
        for i in self.flights_data['prices']:
            try:
                if i['lowestPrice'] >= FlightData(fly_to=i['iataCode']).getPrice():
                    cheapest.append({
                        'city': i['city'],
                        'price': FlightData(fly_to=i['iataCode']).getPrice(),
                        'departure_city_name': FlightData(fly_to=i['iataCode']).getFlightDetails()['cityFrom'],
                        'departure_airport_code': FlightData(fly_to=i['iataCode']).getFlightDetails()['cityCodeFrom'],
                        'arrival_city_name': FlightData(fly_to=i['iataCode']).getFlightDetails()['cityTo'],
                        'arrival_airport_code': FlightData(fly_to=i['iataCode']).getFlightDetails()['cityCodeTo'],
                        'available_seats': FlightData(fly_to=i['iataCode']).getFlightDetails()['availability']['seats'],
                        'outbound_date': FlightData(fly_to=i['iataCode']).getFlightDetails()['local_departure'][:10],
                        'number_of_days': FlightData(fly_to=i['iataCode']).getFlightDetails()['nightsInDest'],
                        'inbound_date': FlightData(fly_to=i['iataCode']).getFlightDetails()['route'][-1][
                                            'local_arrival'][:10],
                        'link': FlightData(fly_to=i['iataCode']).getFlightDetails()['deep_link'],
                        'stop' : FlightData(fly_to=i['iataCode']).getFlightDetails()['deep_link']
                    })
            except TypeError:
                return FlightData(fly_to=i['iataCode']).getFlightDetails()
            else:
                return cheapest
