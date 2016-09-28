import sys
import click
from pyowm.exceptions.api_call_error import APICallError
from weather import api_keys
from Info_From_API import info_from_api as apI


@click.command()
@click.option('--units', type=click.Choice(['celsius', 'fahrenheit']),
              default='celsius')
@click.option('--api-key', help='API key for OpenWeatherMap')
@click.argument('location')
def main(location, units, api_key):
    """Display the current weather forecast for a location.  Accepted formats
    for the location are: US postal code."""

    # why do we have to set up this key
    if api_key is not None:
        api_keys.set_key(api_key)

    city, state = apI.get_city_state(location)

    try:
        weather = apI.get_weather(city, state)
    except APICallError:
        click.echo('An error occurred while connecting to OpenWeather Map.  '
                   'Make sure your API key is valid.')
        sys.exit()

    temperature_info = weather.get_temperature(units)
    # Display either C or F depending on the units.
    symbol = units[:1].upper()
    temperature = '{} °{}'.format(int(temperature_info['temp']), symbol)
    status = weather.get_status()

    click.echo('Current weather for {}, {}'.format(city, state))
    click.echo('Temperature: {}'.format(temperature))
    click.echo('Status: {}'.format(status))

if __name__ == '__main__':
    main()
