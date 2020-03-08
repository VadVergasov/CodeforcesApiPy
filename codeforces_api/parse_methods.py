"""
Parse methods from codeforces.com
"""
import requests
from lxml import html


class CodeforcesParser:
    def get_solution(self, contest_id, submit_id):
        """
        Returns source code for specified submit.
        """
        solutionPage = requests.get(
            "https://codeforces.com/contest/"
            + str(contest_id)
            + "/submission/"
            + str(submit_id)
        )
        tree2 = html.fromstring(solutionPage.text)
        code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')
        if len(code) == 0:
            raise ValueError("Incorrect contest_id or sumbit_id")
        return code[0].replace("\r", "")
