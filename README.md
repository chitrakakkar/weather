# weather
A command-line program written in Python to display information about the weather.

## Installation

### Download and Install
You will probably want to do this inside a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

```
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install git+git://github.com/masonelmore/weather.git@mason-standalone
```

### API key
You will need to sign up for an account at [OpenWeatherMap](http://openweathermap.org/) to get your API key.  weather looks for the key in the following order: 
* the `--api-key` command line option
* an environment variable named `OWM_API_KEY`
* a "configuration" file

Configuration file location:
* Windows: `%LocalAppData%\weather-py\owm_key`
* Linux/Mac: `~/.config/weather-py/owm_key`

Put the key in that file with nothing else.

## Usage
```
$ weather 30359
Current weather for Atlanta, GA
Temperature: 19 °C
Status: Clear
```
