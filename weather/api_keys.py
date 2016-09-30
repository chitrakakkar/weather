import os
import platform


def configuration_path():
    if platform.system() == 'Windows':
        # Need to find a fallback if the env variable doesn't exist.
        base = os.environ.get('LOCALAPPDATA')
    else:
        base = os.path.expanduser('~/.config')

    if base is None:
        return

    config_path = os.path.join(base, 'weather-py', 'owm_key')
    
    return config_path


def load_from_file():
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
