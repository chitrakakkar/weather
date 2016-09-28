""" Environment variables are a key value pairs that can affect how a program runs.
They need to be set at some point before a process is run so the process can read them in and act accordingly.
A lot of times in production environments your database name and password are set as
environment variables so that information does not end up in a code repository somewhere."""


# The platform module includes the tools for
# learning about the interpreter, operating system,
# and hardware platform where a program is running.
import os
import platform

# this method used to setting up the configuration-file


def configuration_path():
    # platform.system() returns the system/OS-> in this case, 'windows
    if platform.system() == 'Windows':
        # Need to find a fallback(back-up) if the env variable doesn't exist.
        # local-data where the config file stays
        base = os.environ.get('LOCALAPPDATA')
    else:
        base = os.path.expanduser('~\.config') # otherwise expand it to user->

    if base is None:
        return

    # setting the configuration file
    # weather.py=  folder # 'OWm-KEy = file
    config_path = os.path.join(base, 'weather-py', 'owm_key')
    
    return config_path


def load_from_file():
    # contains the configuration settings(weather-py $ key)
    config_path = configuration_path()

    if config_path is None:
        return

    try:
        with open(config_path, 'r') as f:
            key = f.read().strip()
        return key
    except FileNotFoundError:
        return


def load_key():
    from_env = os.environ.get('OWM_API_KEY', None)
    from_file = load_from_file()

    return from_env or from_file or ''


def set_key(key):
    global OWM
    OWM = key


OWM = load_key()
