import sys
import traceback


class RubrikException(Exception):
    """Base class for exceptions in this module."""
    pass


class RubrikConnectionException(RubrikException):
    pass


class InvalidAPIEndPointException(RubrikException):
    pass


class MissingCredentialException(RubrikException):
    pass
