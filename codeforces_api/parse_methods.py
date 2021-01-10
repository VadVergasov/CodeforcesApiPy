"""
Parse methods from codeforces.com
"""
import requests
from lxml import html


class CodeforcesParser:
    def get_solution(self, contest_id, submit_id):
        """
        Returns source code for specified submit.

        contest_id is the id of contest.

        submit_id is the id of sumbission.
        """
        solutionPage = requests.get(
            "https://codeforces.com/contest/"
            + str(contest_id)
            + "/submission/"
            + str(submit_id)
        )
        if int(solutionPage.status_code) != 200:
            raise Exception("Returned not OK code" + str(solutionPage))
        tree2 = html.fromstring(solutionPage.text)
        code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')
        if len(code) == 0:
            raise ValueError("Incorrect contest_id or submit_id" + str(code))
        return code[0].replace("\r", "")
