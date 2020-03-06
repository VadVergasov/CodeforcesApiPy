import random


class CodeforcesApiRequestMaker():

    api_key = ""
    secret = ""
    randomKey = 0
    anonimus = False

    def __init__(self, api_key=None, secret=None, rand=1000000):
        """
        Initializes main variables: api_key, secret, random (default is between 1 and 1000000),
        but when you set it it will be yours.
        """

        if rand == 1000000:
            rand = random.randint(1, 1000000)
        if api_key is None and secret is None:
            self.anonimus = True
        else:
            self.api_key = api_key
            self.secret = secret
            self.anonimus = False
        self.randomKey = rand

    def generate_url(self, method_name, **fields):
        """
        Generates request URL for API.
        """
        if not self.anonimus:
            current_time = time.time()
            fields["apiKey"] = str(self.api_key)
            fields["time"] = str(int(current_time))
            api_signature = str(self.randomKey) + "/" + method_name + "?"
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
                "apiSig=" + str(self.randomKey) + str(hashed_signature.hexdigest())
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
