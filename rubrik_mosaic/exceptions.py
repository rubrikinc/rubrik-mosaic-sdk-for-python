import sys
import traceback


class RubrikException(Exception):
    """Base class for exceptions in this module."""
    pass


class RubrikConnectionException(RubrikException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__suppress_context__ = True


class InvalidAPIEndPointException(RubrikException):
    pass


class MissingCredentialException(RubrikException):
    pass
