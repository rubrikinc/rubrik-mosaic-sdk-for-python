# Copyright 2018 Rubrik, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License prop
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the Rubrik Mosaic SDK Connect class.
"""

import requests
import os
import logging

from .api import Api
from .exceptions import RubrikConnectionException, InvalidAPIEndPointException, MissingCredentialException
from .reporting import Reporting

_REPORTING = Reporting
_API = Api

class Connect(Reporting):
    """This class acts as the base class for the Rubrik Mosaic SDK and serves as the main interaction point
    for its end users. It also contains various helper functions used throughout the SDK.

    Arguments:
        _REPORTING {class} - This class contains methods related to reporting on the operations of the Rubrik Mosaic cluster.
    """

    def __init__(self, node_ip=None, username=None, password=None, port="9090", enable_logging=False):
        """Constructor for the Connect class which is used to initialize the class variables.

        Keyword Arguments:
            node_ip {str} -- The Hostname or IP Address of a node in the Rubrik Mosaic cluster you wish to connect to. If a value is not provided we will check for a `rubrik_mosaic_node_ip` environment variable. (default: {None})
            port {str} -- The Port used to connect to the Rubrik Mosaic cluster. If a value is not provided we will check for a `rubrik_mosaic_port` environment variable. (default: {9090})
            username {str} -- The Username you wish to use to connect to the Rubrik Mosaic cluster. If a value is not provided we will check for a `rubrik_mosaic_username` environment variable. (default: {None})
            password {str} -- The Password you wish to use to connect to the Rubrik Mosaic cluster. If a value is not provided we will check for a `rubrik_mosaic_password` environment variable. (default: {None})
            enable_logging {bool} -- Flag to determine if logging will be enabled for the SDK. (default: {False})
        """

        if enable_logging:
            logging.getLogger().setLevel(logging.DEBUG)

        if node_ip is None:
            node_ip = os.environ.get('rubrik_mosaic_node_ip')
            if node_ip is None:
                raise MissingCredentialException("The Rubrik Mosaic Node IP has not been provided.")
            else:
                self.node_ip = node_ip
        else:
            self.node_ip = node_ip

        self.log("Node IP: {}".format(self.node_ip))

        self.port = port
        port = os.environ.get('rubrik_mosaic_port')
        if port is not None:
            self.port = port

        self.log("Node Port: {}".format(self.port))

        if username is None:
            username = os.environ.get('rubrik_mosaic_username')
            if username is None:
                raise MissingCredentialException("The Rubrik Mosaic Username has not been provided.")
            else:
                self.username = username
                self.log("Username: {}".format(self.username))
        else:
            self.username = username
            self.log("Username: {}".format(self.username))

        if password is None:
            password = os.environ.get('rubrik_mosaic_password')
            if password is None:
                raise MissingCredentialException("The Rubrik Mosaic Password has not been provided.")
            else:
                self.password = password
                self.log("Password: *******\n")
        else:
            self.password = password
            self.log("Password: *******\n")

    @staticmethod
    def log(log_message):
        """Create properly formatted debug log messages.

        Arguments:
            log_message {str} -- The message to pass to the debug log.
        """
        log = logging.getLogger(__name__)
        log.debug(log_message)

    def _authorization_header(self):
        """Internal method used to create the authorization header used in the API calls.

        Returns:
            dict -- The authorization header that utilizes token-based authentication.
        """

        config = {}
        config["username"] = self.username
        config["password"] = self.password

        request_url = "https://{}:{}/datos/login".format(self.node_ip, self.port)

        self.log("Generating API Token")

        try:
            api_request = requests.post(request_url, verify=False, data=config, timeout=30)
        except requests.exceptions.ConnectTimeout:
            raise RubrikConnectionException("Unable to establish a connection to the Rubrik Mosaic cluster.")
        except requests.exceptions.ConnectionError:
            raise RubrikConnectionException("Unable to establish a connection to the Rubrik Mosaic cluster.")
        except requests.exceptions.ReadTimeout:
            raise RubrikConnectionException(
                "The Rubrik Mosaic cluster did not respond to the API request in the allotted amount of time. To fix this issue, increase the timeout value.")
        except requests.exceptions.RequestException as error:
            # If "error_message" has be defined raise an exception with that message else
            # raise an exception with the request exception error
            try:
                error_message
            except NameError:
                raise RubrikConnectionException(error)
            else:
                raise RubrikConnectionException(error_messageer)

        api_response = api_request.json()

        api_token = api_response["data"]["token"]

        self.log("API Token: {}".format(api_token))

        authorization_header = {
            'Content-Type': 'application/json',
            "x-access-token": api_token,
        }

        return authorization_header

    @staticmethod
    def _api_validation(api_endpoint):
        """Internal method used to validate the API Version and API Endpoint provided by the end user

        Arguments:

            api_endpoint {str} -- The endpoint of the Rubrik Mosaic API to call (ex. /login).
        """
        # Validate the API Endpoint Syntax
        if not isinstance(api_endpoint, str):
            raise InvalidAPIEndPointException("The API Endpoint must be a string.")
        elif api_endpoint[0] != "/":
            raise InvalidAPIEndPointException("The API Endpoint must begin with '/'. (ex: /adduser)")
