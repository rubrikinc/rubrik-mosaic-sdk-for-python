import sys
import traceback


class RubrikException(Exception):
    """Base class for exceptions in this module."""
    pass


class RubrikConnectionException(RubrikException):


class InvalidAPIEndPointException(RubrikException):
    pass


class MissingCredentialException(RubrikException):
    pass
