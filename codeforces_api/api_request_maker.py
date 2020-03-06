import random


class CodeforcesApiRequestMaker():

    api_key = ""
    secret = ""
    rand = 0
    anonimus = False

    def __init__(self, api_key=None, secret=None, rando=1000000):
        """
        Initializes main variables: api_key, secret, random (default is between 100000
        and 1000000 unless specified)
        """

        if rando >= 1000000 or rando <= 99999:
            rando = random.randint(100000, 999999)
        if api_key is None and secret is None:
            self.anonimus = True
        else:
            self.api_key = api_key
            self.secret = secret
            self.anonimus = False
        self.rand = rando

    def generate_url(self, method_name, **fields):
        """
        Generates request URL for API.
        """

        if not self.anonimus:

            #Renew Rand
            self.renew_rand()

            current_time = time.time()
            fields["apiKey"] = str(self.api_key)
            fields["time"] = str(int(current_time))
            api_signature = str(self.rand) + "/" + method_name + "?"
            fields = collections.OrderedDict(sorted(fields.items()))
            for i in fields:
                api_signature += str(i) + "="
                if isinstance(fields[i], list):
                    for j in fields[i]:
                        api_signature += str(j) + ";"
                else:
                    api_signature += str(fields[i])
                api_signature += "&"
            api_signature = api_signature[:-1]
            api_signature += "#" + str(self.secret)
            hashed_signature = hashlib.sha512(api_signature.encode("utf-8"))

            request_url = "https://codeforces.com/api/" + str(method_name) + "?"
            for i in fields:
                request_url += str(i) + "="
                if isinstance(fields[i], list):
                    for j in fields[i]:
                        request_url += str(j) + ";"
                else:
                    request_url += str(fields[i])
                request_url += "&"
            request_url += (
                "apiSig=" + str(self.rand) + str(hashed_signature.hexdigest())
            )
        else:
            request_url = "https://codeforces.com/api/" + str(method_name) + "?"
            for i in fields:
                request_url += str(i) + "="
                if isinstance(fields[i], list):
                    for j in fields[i]:
                        request_url += str(j) + ";"
                else:
                    request_url += str(fields[i])
                request_url += "&"
            request_url = request_url[:-1]
        return request_url

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

    def renew_rand(self, rando=1000000):
        """
        It's recommended that you renew your apiSig for each request
        default is between 100000 and 1000000 unless specified)
        """
        if rando >= 1000000 or rando <= 99999:
            rando = random.randint(100000, 999999)
        self.rand = rando
