"""
Parse methods from codeforces.com
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
from lxml import html

from codeforces_api.api_requests import CodeforcesApi


class CodeforcesParser:

    session = None
    problem_tags = dict()

    def __init__(self):
        """
        Initializing class. All we will need is a session to optimize performance.
        """
        self.session = requests.Session()

    def get_solution(self, contest_id, submit_id):
        """
        Returns source code for specified submit.

        contest_id is the id of contest.

        submit_id is the id of sumbission.
        """
        solutionPage = self.session.get(
            "https://codeforces.com/contest/"
            + str(contest_id)
            + "/submission/"
            + str(submit_id)
        )
        if int(solutionPage.status_code) != 200:
            raise Exception("Returned not OK code " + str(solutionPage))
        tree2 = html.fromstring(solutionPage.text)
        code = tree2.xpath("//pre[@id='program-source-text']/text()")
        if len(code) == 0:
            raise ValueError("Incorrect contest_id or submit_id " + str(code))
        return code[0].replace("\r", "")

    def get_tags(self, contest_id, index, include_rating=False):
        """
        Get tags of the given problem.

        contest_id is the number of the contest.

        index is the number of the problem, better to be a capital letter. Also could be an integer or lowercase letter.

        include_rating is bool which indicates include or not task rating.
        """
        if self.problem_tags == dict():
            cf_api = CodeforcesApi()
            for problem in cf_api.problemset_problems()["problems"]:
                if str(problem.contest_id) not in self.problem_tags.keys():
                    self.problem_tags[str(problem.contest_id)] = dict()
                self.problem_tags[str(problem.contest_id)][
                    str(problem.index)
                ] = problem.tags
                if include_rating:
                    try:
                        self.problem_tags[str(problem.problem_id)][
                            str(problem.index)
                        ].append("*" + str(problem.rating))
                    except KeyError:
                        pass
        if isinstance(index, int):
            index = chr(ord("A") + index)
        elif isinstance(index, str):
            if index.isnumeric():
                index = chr(ord("A") + int(index))
            index = index.capitalize()
        try:
            return self.problem_tags[str(contest_id)][index]
        except KeyError:
            return self.problem_tags[str(int(contest_id) - 1)][index]
