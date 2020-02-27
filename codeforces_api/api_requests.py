"""
Main class for requests.
"""
import collections
import hashlib
import random
import time

import requests


class CodeforcesApi:
    """
    Class for using official API requests.
    """

    api_key = ""
    secret = ""
    random = 0
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
        self.random = rand

    def generate_url(self, method_name, **fields):
        """
        Generates request URL for API.
        """
        if not self.anonimus:
            current_time = time.time()
            fields["apiKey"] = str(self.api_key)
            fields["time"] = str(int(current_time))
            api_signature = str(self.random) + "/" + method_name + "?"
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
                "apiSig=" + str(self.random) + str(hashed_signature.hexdigest())
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

    def blog_entry_comments(self, blog_entry_id):
        """
        Get blogEntry.commnets for blog, blog_entry_id required.
        Returns parsed response from codeforces.com.
        """
        request = requests.get(
            self.generate_url(
                "blogEntry.comments", **{"blogEntryId": str(blog_entry_id)}
            )
        )
        response = request.json()
        self.check_return_code(response)
        return response

    def blog_entry_view(self, blog_entry_id):
        """
        Get blogEntry.view for blog, blog_entry_id required.
        Returns parsed response from codeforces.com.
        """
        request_url = self.generate_url(
            "blogEntry.view", **{"blogEntryId": str(blog_entry_id)}
        )
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def contest_hacks(self, contest_id):
        """
        Get contest.hacks for contest, contest_id required.
        Returns parsed response from codeforces.com.
        """
        request_url = self.generate_url(
            "contest.hacks", **{"contestId": str(contest_id)}
        )
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def contest_list(self, gym=False):
        """
        Get all contests, you can get all gym by gym parameter.
        Returns parsed response from codeforces.com
        """
        request_url = self.generate_url("contest.list", **{"gym": str(gym)})
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def contest_rating_changes(self, contest_id):
        """
        Get contest.ratingChanges for contest, contest_id required.
        Returns parsed response from codeforces.com.
        """
        request_url = self.generate_url(
            "contest.ratingChanges", **{"contestId": str(contest_id)}
        )
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def contest_standings(
        self,
        contest_id,
        start=-1,
        count=-1,
        handles=[""],
        room=-1,
        show_unofficial=False,
    ):
        """
        Get contest.standings for contest, contest_id required.
        From is replaced with a start, because from is reserved python word.
        Count defines how many submits will be returned.
        Handles should be a list of handles to get (max 10000).
        Room is the number of the room which is needed.
        Show_unofficial is used for adding or removing not official participants.
        Returns parsed response from codeforces.com.
        """
        if not isinstance(handles, list):
            raise TypeError("Handles should be a list")
        if len(handles) > 10000:
            raise OverflowError(
                "Max count of handles should be less or equal to 10000."
            )
        parameters = {
            "contestId": str(contest_id),
            "showUnofficial": str(show_unofficial),
        }
        if start != -1:
            parameters["start"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        if handles != [""]:
            parameters["handles"] = handles
        if room != -1:
            parameters["room"] = str(room)
        request_url = self.generate_url("contest.standings", **parameters)
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def contest_status(self, contest_id, handle="", start=-1, count=-1):
        """
        Get contest.status for contest, contest_id required.
        From is replaced with a start, because from is reserved python word.
        Count defines how many submits will be returned.
        Handle is used for specifying a user.
        Returns parsed response from codeforces.com.
        """
        if contest_id == None:
            raise TypeError("Contest_id is required")
        parameters = {"contestId": str(contest_id)}
        if handle != "":
            parameters["handle"] = handle
        if start != -1:
            parameters["start"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        request_url = self.generate_url("contest.status", **parameters)
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def problemset_problems(self, tags=[""], problemset_name=""):
        """
        Get problemset.problems.
        tags is a list of tags for tasks.
        problemset_name is a string with an additional archive name.
        For example 'acmsguru'.
        Returns parsed response from codeforces.com.
        """
        if not isinstance(tags, list):
            raise TypeError("Tags should be a list")
        parameters = {}
        if tags != [""]:
            parameters["tags"] = tags
        if problemset_name != "":
            parameters["problemsetName"] = problemset_name
        request_url = self.generate_url("problemset.problems", **parameters)
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def problemset_recent_status(self, count, problemset_name=""):
        """
        Get problemset.recentStatus.
        count is the number of returned submits, up to 1000.
        problemset_name is a string with an additional archive name.
        For example 'acmsguru'.
        Returns parsed response from codeforces.com.
        """
        if count > 1000:
            raise OverflowError("Count should be less or equal to 1000")
        parameters = {
            "count": str(count),
        }
        if problemset_name != "":
            parameters["problemsetName"] = problemset_name
        request_url = self.generate_url("problemset.recentStatus", **parameters)
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def recent_actions(self, max_count=100):
        """
        Get recentActions.
        Max_count is the number of returned actions.
        Max_count should be less or equal to 100.
        Returns parsed response from codeforces.com.
        """
        if max_count > 100:
            raise OverflowError("Max_count should be less or equal to 1000")
        request_url = self.generate_url("recentActions", **{"maxCount": str(max_count)})
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def user_blog_entries(self, handle):
        """
        Get user.blogEntries.
        Handle is required.
        Returns parsed response from codeforces.com.
        """
        if handle == "":
            raise TypeError("Handle should not be empty")
        request_url = self.generate_url("user.blogEntries", **{"handle": str(handle)})
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def user_friends(self, only_online=False):
        """
        Get user.friends.
        Auth is required for this method, so create a class instance with api_key and secret.
        Only_online should be boolean.
        Returns parsed response from codeforces.com.
        """
        if self.anonimus:
            raise TypeError("Auth is required.")
        request_url = self.generate_url(
            "user.friends", **{"onlyOnline": str(only_online)}
        )
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def user_info(self, handles):
        """
        Get user.info.
        Handles should be a list of users, up to 10000.
        Returns parsed response from codeforces.com.
        """
        if not isinstance(handles, list):
            raise TypeError("Handles should be a list")
        if len(handles) > 10000:
            raise OverflowError("Max count of handles should be less or equal to 10000")
        request_url = self.generate_url("user.info", **{"handles": handles})
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def user_rated_list(self, active_only=False):
        """
        Get user.ratedList.
        Active_only is used to show only users, which participated last month.
        Returns parsed response from codeforces.com.
        """
        request_url = self.generate_url(
            "user.ratedList", **{"activeOnly": str(active_only)}
        )
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def user_rating(self, handle):
        """
        Get user.rating.
        Handle should be a string.
        Returns parsed response from codeforces.com.
        """
        request_url = self.generate_url("user.rating", **{"handle": str(handle)})
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

    def user_status(self, handle, start=-1, count=-1):
        """
        Get user.status.
        Handle is required.
        From was replaced with a start because from is reserved python word.
        Count is the number of attempts to return.
        Returns parsed response from codeforces.com.
        """
        parameters = {
            "handle": str(handle),
        }
        if start != -1:
            parameters["start"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        request_url = self.generate_url("user.status", **parameters)
        request = requests.get(request_url)
        response = request.json()
        self.check_return_code(response)
        return response

