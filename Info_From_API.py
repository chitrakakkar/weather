from pyowm import OWM
from weather import api_keys
from weather.lib import Ziptastic


class info_from_api:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_city_state(self, postal_code):
        api = Ziptastic('')
        location = api.get_from_postal_code(postal_code)
        city, state = location['city'], location['state']
        return city, state

    def get_weather(self, city, state):
        """Return the weather at the city, state."""

        # OWM expects the place to be in the format of CITY,COUNTRY (Minneapolis,
        #  US).  The only problem with that is some cities like Bloomington are
        # ambiguous.  Querying the API with CITY,STATE (Minneapolis,Minnesota)
        # seems to work.  I don't think there are any two-character state codes
        # that clash with any countries.  We should probably expect bug reports,
        # though.
        api = OWM(api_keys.OWM)
        place = '{},{}'.format(city, state)
        observation = api.weather_at_place(place)
        weather = observation.get_weather()

        return weather

