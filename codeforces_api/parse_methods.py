"""
Parse methods from codeforces.com
"""
import requests
from lxml import html
from codeforces_api.api_requests import CodeforcesApi


class CodeforcesParser:

    session = None
    problem_tags = dict()

    def __init__(self):
        """
        Initializing class. All we will need is session to optimize performance.
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

    def get_tags(self, contest_id, index):
        """
        Get tags of given problem.

        contest_id is number of contest.

        index is number of problem, better to be capital letter. Also could be integer or lowercase letter.
        """
        if self.problem_tags == dict():
            cf_api = CodeforcesApi()
            for problem in cf_api.problemset_problems()["result"]["problems"]:
                if str(problem["contestId"]) not in self.problem_tags.keys():
                    self.problem_tags[str(problem["contestId"])] = dict()
                self.problem_tags[str(problem["contestId"])][
                    str(problem["index"])
                ] = problem["tags"]
        if isinstance(index, int):
            index = chr(ord("A") + index)
        elif isinstance(index, str):
            if index.isnumeric():
                index = chr(ord("A") + int(index))
            index = index.capitalize()
        return self.problem_tags[str(contest_id)][index]
