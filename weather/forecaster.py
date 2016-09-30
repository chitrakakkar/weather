from pyowm import OWM
from weather.lib import Ziptastic
from weather import api_keys

""" extract Forecaster object with the help of OWM API"""


class Forecaster:
    def __init__(self, postal_code, units):
        self.postal_code = postal_code
        self.units = units
        self.city, self.state = self.get_city_state()
        self.weather = self.get_current_weather()

    def get_current_weather(self):

        api = OWM(api_keys.OWM)
        place = '{},{}'.format(self.city, self.state)
        observation = api.weather_at_place(place)
        current_weather = observation.get_weather()

        return current_weather

    def get_city_state(self):
        api = Ziptastic('')
        #Location returns a json object
        location = api.get_from_postal_code(self.postal_code)
        if location.get('message', None) == 'Not Found':
            raise PostalCodeNotFound
        city, state = location['city'], location['state']
        return city, state

    def display_weather(self, print_func):
        temperature_info = self.weather.get_temperature(self.units)
        # Display either C or F depending on the units.
        # slicing the unit string(celsius as default-> Returns 'C')
        symbol = self.units[:1].upper()
        temperature = '{} °{}'.format(int(temperature_info['temp']), symbol)
        status = self.weather.get_status()
        print_func('Current weather for {}, {}'.format(self.city, self.state))
        print_func('Temperature: {}'.format(temperature))
        print_func('Status: {}'.format(status))


class PostalCodeNotFound(Exception):
    """Raised when an invalid postal code is passed to the program."""

