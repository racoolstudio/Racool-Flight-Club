from data_manager import *
from datetime import *
from dateutil.relativedelta import relativedelta
import os
from requests import *


class FlightData:
    '''This class is responsible for structuring the flight data.'''

    def __init__(self, fly_to, fly_from='YYT', max_length_of_stay=25, flight_type='round', num_of_adult=1,
                 num_of_children=0, min_length_of_stay=7, ):
        self.api = os.getenv('SEARCHAPI')
        self.URL = 'https://tequila-api.kiwi.com/v2/search'
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.today = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')
        self.end_date = (datetime.now() + relativedelta(months=6)).strftime('%d/%m/%Y')
        self.return_from = fly_to
        self.return_to = fly_from
        self.flight_type = flight_type
        self.adult = num_of_adult
        self.child = num_of_children
        self.nights_in_dst_from = min_length_of_stay
        self.nights_in_dst_to = max_length_of_stay
        self.curr = 'CAD'
        self.header = {
            'apikey': self.api,

        }

    def getFlightDetails(self):
        parameter = {
            'fly_from': self.fly_from,
            'fly_to': self.fly_to,
            'date_from': self.today,
            'date_to': self.end_date,
            'children': self.child,
            'curr': self.curr,
            'nights_in_dst_from': self.nights_in_dst_from,
            'nights_in_dst_to': self.nights_in_dst_to,


        }
        try:
            detail = get(url=self.URL, headers=self.header, params=parameter).json()['data'][0]
        except IndexError:
            return f'There are no Flights Available for {self.fly_to}'
        else:
            return detail

    def getPrice(self):

        try:
            prices = self.getFlightDetails()['price']
        except TypeError:
            return 0
        else:
            return prices
