"""
The main class for the API requests.
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
import requests

from codeforces_api.api_request_maker import CodeforcesApiRequestMaker
from codeforces_api.types import (
    BlogEntry,
    Comment,
    Contest,
    Hack,
    Problem,
    ProblemStatistic,
    RanklistRow,
    RatingChange,
    RecentAction,
    Submission,
    User,
)


class CodeforcesApi(CodeforcesApiRequestMaker):
    """
    Class for using official API requests.
    """

    session = None
    method = None

    def _make_request(self, method, **payload):
        """
        Making request to codeforces.com

        Uses different methods (POST or GET) but be aware of 413 error when using GET.
        """
        request_data = self.generate_request(method, **payload)
        request = self.session.request(
            self.method, request_data["request_url"], data=request_data["data"]
        )
        if request.status_code == 502:
            raise SystemError("Codeforces is unavailable now.")
        return self.get_response(request)

    def __init__(self, api_key=None, secret=None, random_number=1000000, method="POST"):
        """
        Initializing class. All we will need is a session to optimize performance.
        """
        super().__init__(api_key, secret, random_number)
        self.session = requests.Session()
        if method == "POST" or method == "GET":
            self.method = method
        else:
            raise ValueError("method should be POST or GET")

    def blog_entry_comments(self, blog_entry_id):
        """
        Get blogEntry.commnets for blog, blog_entry_id required.

        Returns parsed response from codeforces.com.
        """
        return [
            Comment.de_json(comment)
            for comment in self._make_request(
                "blogEntry.comments", **{"blogEntryId": str(blog_entry_id)}
            )
        ]

    def blog_entry_view(self, blog_entry_id):
        """
        Get blogEntry.view for blog, blog_entry_id required.

        Returns parsed response from codeforces.com.
        """
        return BlogEntry.de_json(
            self._make_request("blogEntry.view", **{"blogEntryId": str(blog_entry_id)})
        )

    def contest_hacks(self, contest_id):
        """
        Get contest.hacks for contest, contest_id required.

        Returns parsed response from codeforces.com.
        """
        return [
            Hack.de_json(hack)
            for hack in self._make_request(
                "contest.hacks", **{"contestId": str(contest_id)}
            )
        ]

    def contest_list(self, gym=False):
        """
        Get all contests you can get all gym by gym parameter.

        Returns parsed response from codeforces.com
        """
        return [
            Contest.de_json(contest)
            for contest in self._make_request(
                "contest.list", **{"gym": str(gym).lower()}
            )
        ]

    def contest_rating_changes(self, contest_id):
        """
        Get contest.ratingChanges for the contest, contest_id required.

        Returns parsed response from codeforces.com.
        """
        return [
            RatingChange.de_json(rating_change)
            for rating_change in self._make_request(
                "contest.ratingChanges", **{"contestId": str(contest_id)}
            )
        ]

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

        count defines how many submits will be returned.

        handles should be a list of handles to get (max 10000).

        room is the number of the room which is needed.

        show_unofficial is used for adding or removing not official participants.

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
            "showUnofficial": str(show_unofficial).lower(),
        }
        if start != -1:
            parameters["start"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        if handles != [""]:
            handles_str = ""
            for handle in handles:
                handles_str += str(handle) + ";"
            parameters["handles"] = handles_str
        if room != -1:
            parameters["room"] = str(room)
        response = self._make_request("contest.standings", **parameters)
        result = {
            "contest": Contest.de_json(response["contest"]),
            "problems": [],
            "rows": [],
        }
        for problem in response["problems"]:
            result["problems"].append(Problem.de_json(problem))
        for row in response["rows"]:
            result["rows"].append(RanklistRow.de_json(row))
        return result

    def contest_status(self, contest_id, handle="", start=-1, count=-1):
        """
        Get contest.status for contest, contest_id required.

        From is replaced with a start, because from is reserved python word.

        count defines how many submits will be returned.

        handle is used for specifying a user.

        Returns parsed response from codeforces.com.
        """
        if contest_id is None:
            raise TypeError("Contest_id is required")
        parameters = {"contestId": str(contest_id)}
        if handle != "":
            parameters["handle"] = handle
        if start != -1:
            parameters["start"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        return [
            Submission.de_json(submission)
            for submission in self._make_request("contest.status", **parameters)
        ]

    def problemset_problems(self, tags=[""], problemset_name=""):
        """
        Get problemset.problems.

        tags is a list of tags for tasks.

        problemset_name is a string with an additional archive name. For example 'acmsguru'.

        Returns parsed response from codeforces.com.
        """
        if not isinstance(tags, list):
            raise TypeError("Tags should be a list")
        parameters = {}
        if tags != [""]:
            parameters["tags"] = tags
        if problemset_name != "":
            parameters["problemsetName"] = problemset_name
        result = {"problems": [], "problem_statistics": []}
        response = self._make_request("problemset.problems", **parameters)
        for problem in response["problems"]:
            result["problems"].append(Problem.de_json(problem))
        for problem_statistic in response["problemStatistics"]:
            result["problem_statistics"].append(
                ProblemStatistic.de_json(problem_statistic)
            )
        return result

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
        return [
            Submission.de_json(submission)
            for submission in self._make_request(
                "problemset.recentStatus", **parameters
            )
        ]

    def recent_actions(self, max_count=100):
        """
        Get recentActions.

        max_count is the number of returned actions.

        max_count should be less or equal to 100.

        Returns parsed response from codeforces.com.
        """
        if max_count > 100:
            raise OverflowError("Max_count should be less or equal to 1000")
        return [
            RecentAction.de_json(recent_action)
            for recent_action in self._make_request(
                "recentActions", **{"maxCount": str(max_count)}
            )
        ]

    def user_blog_entries(self, handle):
        """
        Get user.blogEntries.

        handle is required.

        Returns parsed response from codeforces.com.
        """
        if handle == "":
            raise TypeError("Handle should not be empty")
        return [
            BlogEntry.de_json(blog_entry)
            for blog_entry in self._make_request(
                "user.blogEntries", **{"handle": str(handle)}
            )
        ]

    def user_friends(self, only_online=False):
        """
        Get user.friends.

        Auth is required for this method, so create a class instance with api_key and secret.

        only_online should be boolean.

        Returns parsed response from codeforces.com.
        """
        if self.anonimus:
            raise TypeError("Auth is required.")
        return self._make_request(
            "user.friends", **{"onlyOnline": str(only_online).lower()}
        )

    def user_info(self, handles):
        """
        Get user.info.

        handles should be a list of users, up to 10000.

        Returns parsed response from codeforces.com.
        """
        if not isinstance(handles, list):
            raise TypeError("Handles should be a list")
        if len(handles) > 10000:
            raise OverflowError("Max count of handles should be less or equal to 10000")
        handles_str = ""
        for handle in handles:
            handles_str += str(handle) + ";"
        return [
            User.de_json(user)
            for user in self._make_request("user.info", **{"handles": handles_str})
        ]

    def user_rated_list(self, active_only=False):
        """
        Get user.ratedList.

        active_only is used to show only users, which participated last month.

        Returns parsed response from codeforces.com.
        """
        return [
            User.de_json(user)
            for user in self._make_request(
                "user.ratedList", **{"activeOnly": str(active_only).lower()}
            )
        ]

    def user_rating(self, handle):
        """
        Get user.rating.

        handle should be a string.

        Returns parsed response from codeforces.com.
        """
        return [
            RatingChange.de_json(rating_change)
            for rating_change in self._make_request(
                "user.rating", **{"handle": str(handle)}
            )
        ]

    def user_status(self, handle, start=-1, count=-1):
        """
        Get user.status.

        handle is required.

        From was replaced with a start because from is reserved python word.

        count is the number of attempts to return.

        Returns parsed response from codeforces.com.
        """
        parameters = {
            "handle": str(handle),
        }
        if start != -1:
            parameters["from"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        return [
            Submission.de_json(submission)
            for submission in self._make_request("user.status", **parameters)
        ]
