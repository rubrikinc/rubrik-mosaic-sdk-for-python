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
This module contains the Rubrik SDK API class.
"""

import requests
import json
import time
try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+
from random import choice

from .exceptions import RubrikConnectionException


class Api():
    """This class contains the base API methods that can be called independently or internally in standalone functions."""

    def __init__(self, node_ip):
        super().__init__(node_ip)

    def _common_api(self, call_type, api_endpoint, config=None, timeout=15, params=None):
        """Internal method that consolidates the base API functions.

        Arguments:
            call_type {str} -- The HTTP Method for the type of RESTful API call being made. (choices: {'GET', 'POST', 'TOKEN_GENERATE'.})
            api_endpoint {str} -- The endpoint of the Rubrik CDM API to call (ex. /cluster/me).

        Keyword Arguments:
            params {dict} -- An optional dict containing variables in a key:value format to send with `GET` & `DELETE` API calls (default: {None})
            timeout {int} -- The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error. (default: {15})

        Returns:
            dict -- The full API call response for the provided endpoint.
        """

        self._api_validation(api_endpoint)

        header = self._authorization_header()

        request_url = "https://{}:{}/datos{}".format(self.node_ip, self.port, api_endpoint)

        try:
            # Determine which call type is being used and then set the relevant
            # variables for that call type
            if call_type == 'GET':

                if params is not None:
                    request_url = request_url + "?" + '&'.join("{}={}".format(key, val)
                                                               for (key, val) in params.items())
                request_url = quote(request_url, '://?=&')
                self.log('GET {}'.format(request_url))
                api_request = requests.get(request_url, verify=False, headers=header, timeout=timeout)

            else:
                # config = json.dumps(config)
                self.log('POST {}'.format(request_url))
                self.log('Config {}'.format(config))

                self.log(type(config))

                api_request = requests.post(request_url, verify=False, headers=header, json=config, timeout=timeout)

            self.log(str(api_request) + "\n")
            try:
                api_response = api_request.json()
                # Check to see if an error message has been provided by Rubrik
                for key, value in api_response.items():
                    if key == "errorType" or key == 'message':
                        error_message = api_response['message']
                        api_request.raise_for_status()

            except BaseException:
                api_request.raise_for_status()
        except requests.exceptions.ConnectTimeout:
            raise RubrikConnectionException("Unable to establish a connection to the Rubrik cluster.") from None
        except requests.exceptions.ConnectionError:
            raise RubrikConnectionException("Unable to establish a connection to the Rubrik cluster.") from None
        except requests.exceptions.ReadTimeout:
            raise RubrikConnectionException(
                "The Rubrik cluster did not respond to the API request in the allotted amount of time. To fix this issue, increase the timeout value.") from None
        except requests.exceptions.RequestException as error:
            # If "error_message" has be defined raise an exception for that message else
            # raise an exception for the request exception error
            try:
                error_message
            except NameError:
                raise RubrikConnectionException(error) from None
            else:
                raise RubrikConnectionException(error_messageer)
        else:
            try:
                return api_request.json()
            except BaseException:
                return {'status_code': api_request.status_code}

    def get(self, api_endpoint, timeout=15, params=None):
        """Send a GET request to the provided Rubrik API endpoint.

        Arguments:
            api_endpoint {str} -- The endpoint of the Rubrik CDM API to call (ex. /listjobs).

        Keyword Arguments:
            params {dict} -- An optional dict containing variables in a key:value format to send with `GET` & `DELETE` API calls (default: {None})
            timeout {int} -- The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error. (default: {15})

        Returns:
            dict -- The response body of the API call.
        """

        return self._common_api('GET', api_endpoint, config=None, timeout=timeout, params=params)

    def post(self, api_endpoint, config, timeout=15):
        """Send a POST request to the provided Rubrik API endpoint.

        Arguments:
            api_endpoint {str} -- The endpoint of the Rubrik CDM API to call (ex. /listjobs).

        Keyword Arguments:
            timeout {int} -- The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error. (default: {15})

        Returns:
            dict -- The response body of the API call.
        """

        return self._common_api('POST', api_endpoint, config, timeout=timeout)
