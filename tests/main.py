"""
Testing module work.
"""

import codeforces_api
import conf
import time

MAIN = codeforces_api.CodeforcesApi(conf.API_KEY, conf.API_SECRET)

PARSER = codeforces_api.CodeforcesParser()

COMMENTS = MAIN.blog_entry_comments(74185)
VIEW = MAIN.blog_entry_view(74185)
HACKS = MAIN.contest_hacks(1311)
LIST = MAIN.contest_list()
RATING_CHANGES = MAIN.contest_rating_changes(1311)
time.sleep(1)
STANDINGS = MAIN.contest_standings(1311, handles=["tourist", "VadVergasov"])
STATUS = MAIN.contest_status(1311)
PROBLEMS = MAIN.problemset_problems()
RECENT_STATUS = MAIN.problemset_recent_status(10)
RECENT_ACTIONS = MAIN.recent_actions()
time.sleep(1)
USER_ENTRIES = MAIN.user_blog_entries("VadVergasov")
FRIENDS = MAIN.user_friends(True)
INFO = MAIN.user_info(["tourist", "VadVergasov"])
RATINGS = MAIN.user_rated_list(True)
USER_RATING = MAIN.user_rating("VadVergasov")
time.sleep(1)
USER_STATUS = MAIN.user_status("VadVergasov")

SOLUTION = PARSER.get_solution(1322, 72628149)

print("No errors found!")
