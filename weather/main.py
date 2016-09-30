import sys
import click
from weather.exceptions import *
from weather.forecaster import Forecaster
from weather import api_keys


@click.command()
@click.option('--units', type=click.Choice(['celsius', 'fahrenheit']),
              default='celsius')
@click.option('--api-key', help='API key for OpenWeatherMap')
@click.argument('postal_code')
def main(postal_code, units, api_key):
    """Display the current weather forecast for a US postal code."""

    if api_key is not None:
        api_keys.set_key(api_key)

    try:
        forecaster = Forecaster(postal_code, units)
        forecaster.display_weather(click.echo)
    except PostalCodeNotFound:
        click.echo('Error:{} is not a valid US postal code'.format(postal_code))
        sys.exit()
    except APICallError:
        click.echo('An error occurred while connecting to OpenWeather Map.  '
                   'Make sure your API key is valid.')
        sys.exit()

if __name__ == '__main__':
    main()
