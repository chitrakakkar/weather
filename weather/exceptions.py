from pyowm.exceptions.api_call_error import APICallError


class PostalCodeNotFound(Exception):
    """Raised when an invalid postal code is passed to the program."""
