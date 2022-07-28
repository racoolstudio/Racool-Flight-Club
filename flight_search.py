import os

from requests import *

location_endpoint = 'https://tequila-api.kiwi.com/locations/query'
flight_api = os.getenv('FLIGHTAPI')
header = {
    'apikey': flight_api
}


# definition of the class starts here
class FlightSearch:

    # defining constructor
    def __init__(self, city):
        self.city = city
        self.parameter = {'term': self.city}
        # defining class methods

    def getCode(self):
        return get(url=location_endpoint, headers=header, params=self.parameter).json()['locations'][0]['code']

