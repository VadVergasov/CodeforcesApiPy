"""
Class for generating request URLs, which includes working with random, unpacking parameters, calculating hashes.
Copyright (C) 2021 Vadim Vergasov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import collections
import hashlib
import json
import random
import time

import requests


class CodeforcesApiRequestMaker:

    _api_key = None
    _secret = None
    _rand = 0
    assigned_rand = False
    anonimus = False

    def __init__(self, api_key=None, secret=None, random_number=1000000):
        """
        Initializes main variables: api_key, secret, random (default is between 1
        and 1000000 unless specified)
        """

        if random_number == 1000000:
            random_number = random.randint(100000, 999999)
            self.assigned_rand = True
        elif random_number < 100000 and random_number > 999999:
            raise Exception(
                "The non-6-digit number passed as random_number for API Signature",
                random_number,
            )
        if api_key is None and secret is None:
            self.anonimus = True
        else:
            self._api_key = api_key
            self._secret = secret
            self.anonimus = False
        self._rand = random_number

    def generate_request(self, method_name, **fields):
        """
        Generates request URL and data for API.
        """
        request_url = "https://codeforces.com/api/" + str(method_name)
        if not self.anonimus:
            # Renew Rand
            if not self.assigned_rand:
                self.renew_rand()

            current_time = time.time()
            fields["apiKey"] = str(self._api_key)
            fields["time"] = str(int(current_time))
            api_signature = str(self._rand) + "/" + method_name + "?"
            fields = collections.OrderedDict(sorted(fields.items()))
            api_signature += requests.urllib3.request.urlencode(fields, safe=";")
            api_signature += "#" + str(self._secret)
            hashed_signature = hashlib.sha512(api_signature.encode("utf-8"))
            fields["apiSig"] = str(self._rand) + str(hashed_signature.hexdigest())
        return {"request_url": request_url, "data": fields}

    def check_return_code(self, response):
        """
        Checks if a returned response is OK.

        If not OK Exception will be raised will additional info.
        """
        if response["status"] != "OK":
            raise Exception(
                "Request returned not OK status",
                response["status"],
                response["comment"],
            )

    def renew_rand(self, random_number=1000000):
        """
        It's recommended that you renew your apiSig for each request
        default is between 100000 and 1000000 unless specified)
        """
        if random_number == 1000000:
            random_number = random.randint(100000, 999999)
        elif random_number < 100000 and random_number > 999999:
            raise Exception(
                "The non-6-digit number passed as random_number for renew_rand",
                random_number,
            )

    def get_response(self, request):
        if request.status_code != 200:
            raise Exception("Server returned status code: " + str(request.status_code))
        try:
            response = request.json()
            self.check_return_code(response)
            return response["result"]
        except json.decoder.JSONDecodeError as error:
            raise ValueError(
                "A lot of users, try to reduce the number of users in the list.\nError: %s.\nResponse text: %s"
                % (str(error), request.text)
            )
