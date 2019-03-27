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
This module contains the Rubrik SDK Connect class.
"""

import base64
import requests
import sys
import os
import logging
from random import choice
import time

from .api import Api


_CLUSTER = Cluster
_DATA_MANAGEMENT = Data_Management
_PHYSICAL = Physical
_API = Api
_CLOUD = Cloud


class Connect(_CLUSTER, _DATA_MANAGEMENT, _PHYSICAL, _CLOUD):
    """This class acts as the base class for the Rubrik SDK and serves as the main interaction point
    for its end users. It also contains various helper functions used throughout the SDK.

    Arguments:
        _CLUSTER {class} -- This class contains methods related to the managment of the Rubrik Cluster itself.
        _DATA_MANAGEMENT {class} - This class contains methods related to backup and restore operations for the various objects managed by the Rubrik Cluster.
        _PHYSICAL {class} - This class contains methods related to the managment of the Physical objects in the Rubrik Cluster.
    """

    def __init__(self, node_ip=None, username=None, password=None, api_token=None, enable_logging=False):
        """Constructor for the Connect class which is used to initialize the class variables.

        Keyword Arguments:
            node_ip {str} -- The Hostname or IP Address of a node in the Rubrik cluster you wish to connect to. If a value is not provided we will check for a `rubrik_cdm_node_ip` environment variable. (default: {None})
            username {str} -- The Username you wish to use to connect to the Rubrik cluster. If a value is not provided we will check for a `rubrik_cdm_username` environment variable. (default: {None})
            password {str} -- The Password you wish to use to connect to the Rubrik cluster. If a value is not provided we will check for a `rubrik_cdm_password` environment variable. (default: {None})
            api_token {str} -- The API Token you wish to use to connect to the Rubrik cluster. If populated, the `username` and `password` fields will be ignored. If a value is not provided we will check for a `rubrik_cdm_token` environment variable.  (default: {None})
            enable_logging {bool} -- Flag to determine if logging will be enabled for the SDK. (default: {False})
        """

        if enable_logging:
            logging.getLogger().setLevel(logging.DEBUG)

        if node_ip is None:
            node_ip = os.environ.get('rubrik_cdm_node_ip')
            if node_ip is None:
                sys.exit("Error: The Rubrik CDM Node IP has not been provided.")
            else:
                self.node_ip = node_ip
        else:
            self.node_ip = node_ip

        self.log("Node IP: {}".format(self.node_ip))

        # If the api_token has not been provided check for the env variable and then
        # check for the username and password fields
        if api_token is None:
            api_token = os.environ.get('rubrik_cdm_token')
            if api_token is None:

                self.api_token = None

                if username is None:
                    username = os.environ.get('rubrik_cdm_username')
                    if username is None:
                        sys.exit("Error: The Rubrik CDM Username or an API Token has not been provided.")
                    else:
                        self.username = username
                        self.log("Username: {}".format(self.username))
                else:
                    self.username = username
                    self.log("Username: {}".format(self.username))

                if password is None:
                    password = os.environ.get('rubrik_cdm_password')
                    if password is None:
                        sys.exit("Error: The Rubrik CDM Password or an API Token has not been provided.")
                    else:
                        self.password = password
                        self.log("Password: *******\n")
                else:
                    self.password = password
                    self.log("Password: *******\n")

            else:
                self.api_token = api_token
                self.log("API Token: *******\n")
        else:
            self.api_token = api_token
            self.log("API Token: *******\n")

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
            dict -- The authorization header that utilizes Basic authentication.
        """

        if self.api_token is None:
            self.log("Creating the authorization header using the provided username and password.")

            credentials = '{}:{}'.format(self.username, self.password)

            # Encode the Username:Password as base64
            authorization = base64.b64encode(credentials.encode())
            # Convert to String for API Call
            authorization = authorization.decode()

            authorization_header = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Basic ' + authorization,
                'User-Agent': 'Rubrik Python SDK v1.0.13'
            }

        else:

            self.log("Creating the authorization header using the provided API Token.")
            authorization_header = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + self.api_token,
                'User-Agent': 'Rubrik Python SDK v1.0.13'
            }

        return authorization_header

    @staticmethod
    def _header():
        """Internal method used to create the a header without authorization used in the API calls.

        Returns:
            dict -- The header that does not include any authorization.
        """

        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        return header

    @staticmethod
    def _api_validation(api_version, api_endpoint):
        """Internal method used to validate the API Version and API Endpoint provided by the end user

        Arguments:
            api_version {str} -- The version of the Rubrik CDM API to call. (choices: {v1, v2, internal})
            api_endpoint {str} -- The endpoint of the Rubrik CDM API to call (ex. /cluster/me).
        """

        valid_api_versions = ['v1', 'v2', 'internal']

        # Validate the API Version
        if api_version not in valid_api_versions:
            sys.exit(
                "Error: Enter a valid API version {}.".format(valid_api_versions))

        # Validate the API Endpoint Syntax
        if not isinstance(api_endpoint, str):
            sys.exit("Error: The API Endpoint must be a string.")
        elif api_endpoint[0] != "/":
            sys.exit(
                "Error: The API Endpoint should begin with '/'. (ex: /cluster/me)")
        elif api_endpoint[-1] == "/":
            sys.exit(
                "Error: The API Endpoint should not end with '/'. (ex. /cluster/me)")
