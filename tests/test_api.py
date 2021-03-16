"""
Testing requests to api.
"""
from codeforces_api.types import BlogEntry, Comment, Party, Problem
from codeforces_api import CodeforcesApi


def test_blog_entry_comments(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    comments = api.blog_entry_comments(74291)
    for comment in comments:
        if comment.id == 584151:
            assert comment.creation_time_seconds == 1582795345


def test_blog_entry_view(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    blog_entry = api.blog_entry_view(74291)
    assert blog_entry.author_handle == "VadVergasov"
    assert blog_entry.original_locale == "ru"
    assert blog_entry.id == 74291
    assert blog_entry.title == "<p>Codeforces API python</p>"
    assert blog_entry.allow_view_history == True
    assert blog_entry.tags == [
        "#api",
        "api",
        "#codeforces",
        "#python",
        "#python 3",
        "python 3",
    ]
    assert blog_entry.content is None


def test_contest_hacks(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    hacks = api.contest_hacks(1311)
    for hack in hacks:
        if hack.id == 615666:
            assert hack.creation_time_seconds == 1582562199
            assert hack.verdict == "INVALID_INPUT"
            assert hack.judge_protocol == {
                "protocol": "Validator 'validator.exe' returns exit code 3 [FAIL Integer parameter [name=t] equals to 1000, violates the range [1, 100] (stdin, line 1)]",
                "manual": "false",
                "verdict": "Invalid input",
            }
            assert hack.hacker.participant_type == "PRACTICE"
            assert hack.hacker.ghost == False
            assert hack.hacker.members[0].handle == "VietCT"
            assert hack.hacker.team_id is None
            assert hack.hacker.contest_id == 1311
            assert hack.hacker.room is None
            assert hack.hacker.start_time_seconds == 1582554900
            assert hack.defender.members[0].handle == "UMR"
            assert hack.defender.participant_type == "OUT_OF_COMPETITION"
            assert hack.defender.ghost == False
            assert hack.defender.team_id is None
            assert hack.defender.contest_id == 1311
            assert hack.defender.room is None
            assert hack.defender.start_time_seconds == 1582554900
            assert hack.problem.index == "D"
            assert hack.problem.name == "Three Integers"
            assert hack.problem.problem_type == "PROGRAMMING"
            assert hack.problem.contest_id == 1311
            assert hack.problem.problemset_name is None
            assert hack.problem.points is None
            assert hack.problem.rating == 2000
            assert hack.problem.tags == ["brute force", "math"]
            assert hack.test is None
            break


def test_contest_list():
    api = CodeforcesApi()
    list = api.contest_list()
    for contest in list:
        if contest.id == 1496:
            assert contest.name == "Codeforces Round #706 (Div. 2)"
            assert contest.contest_type == "CF"
            assert contest.phase == "FINISHED"
            assert contest.frozen == False
            assert contest.duration_seconds == 7200
            assert contest.start_time_seconds == 1615377900
            assert contest.prepared_by is None
            assert contest.website_url is None
            assert contest.description is None
            assert contest.difficulty is None
            assert contest.kind is None
            assert contest.icpc_region is None
            assert contest.country is None
            assert contest.city is None
            assert contest.season is None
            break


def test_contest_rating_changes(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    changes = api.contest_rating_changes(1313)
    for change in changes:
        if change.handle == "VadVergasov":
            assert change.contest_id == 1313
            assert change.contest_name == "Codeforces Round #622 (Div. 2)"
            assert change.rank == 2303
            assert change.rating_update_time_seconds == 1582455900
            assert change.old_rating == 1330
            assert change.new_rating == 1381
            break


def test_contest_standings(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    standings = api.contest_standings(1313, handles=["VadVergasov"])
    assert standings["contest"].id == 1313
    assert standings["contest"].name == "Codeforces Round #622 (Div. 2)"
    assert standings["contest"].contest_type == "CF"
    assert standings["contest"].phase == "FINISHED"
    assert standings["contest"].frozen == False
    assert standings["contest"].duration_seconds == 7200
    assert standings["contest"].start_time_seconds == 1582448700
    assert standings["contest"].prepared_by is None
    assert standings["contest"].website_url is None
    assert standings["contest"].description is None
    assert standings["contest"].difficulty is None
    assert standings["contest"].kind is None
    assert standings["contest"].icpc_region is None
    assert standings["contest"].country is None
    assert standings["contest"].city is None
    assert standings["contest"].season is None
    for problem in standings["problems"]:
        if problem.index == "A":
            assert problem.name == "Fast Food Restaurant"
            assert problem.problem_type == "PROGRAMMING"
            assert problem.contest_id == 1313
            assert problem.problemset_name is None
            assert problem.points == 500.0
            assert problem.rating == 900
            assert problem.tags == ["brute force", "greedy", "implementation"]
            break
    for row in standings["rows"]:
        if row.party.members[0].handle == "VadVergasov":
            assert row.rank == 2303
            assert row.party.participant_type == "CONTESTANT"
            assert row.party.ghost == False
            assert row.party.team_id is None
            assert row.party.contest_id == 1313
            assert row.party.room == 10
            assert row.party.start_time_seconds == 1582448700
            assert row.points == 1124.0
            assert row.penalty == 0
            assert row.successful_hack_count == 0
            assert row.unsuccessful_hack_count == 0
            for problem in [0, 1, 3, 4, 5]:
                assert row.problem_results[problem].penalty is None
                assert row.problem_results[problem].problem_type == "FINAL"
                assert row.problem_results[problem].rejected_attempt_count == 0
            assert row.last_submission_time_seconds is None
            assert row.problem_results[0].points == 452.0
            assert row.problem_results[0].best_submission_time_seconds == 1466
            assert row.problem_results[2].points == 672.0
            assert row.problem_results[2].rejected_attempt_count == 2
            assert row.problem_results[2].best_submission_time_seconds == 3439
            for problem in [1, 3, 4, 5]:
                assert row.problem_results[problem].points == 0.0
                assert row.problem_results[problem].best_submission_time_seconds is None
            assert row.last_submission_time_seconds is None
            break


def test_contest_status():
    api = CodeforcesApi()
    status = api.contest_status(1313)
    for row in status:
        if row.id == 71660372:
            assert row.creation_time_seconds == 1582450166
            assert row.relative_time_seconds == 1466
            assert row.problem.index == "A"
            assert row.problem.name == "Fast Food Restaurant"
            assert row.problem.problem_type == "PROGRAMMING"
            assert row.problem.contest_id == 1313
            assert row.problem.points == 500.0
            assert row.problem.rating == 900
            assert row.problem.tags == ["brute force", "greedy", "implementation"]
            assert row.author.members[0].handle == "VadVergasov"
            assert row.author.participant_type == "CONTESTANT"
            assert row.author.ghost == False
            assert row.author.team_id is None
            assert row.author.contest_id == 1313
            assert row.author.room == 10
            assert row.author.start_time_seconds == 1582448700
            assert row.programming_language == "GNU C++17"
            assert row.testset == "TESTS"
            assert row.passed_test_count == 5
            assert row.time_consumed_millis == 171
            assert row.memory_consumed_bytes == 0
            assert row.contest_id == 1313
            assert row.verdict == "OK"
            assert row.points is None


def test_problemset_problems(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    problemset = api.problemset_problems()
    for problem in problemset["problems"]:
        if problem.name == "Single Push":
            assert problem.index == "A"
            assert problem.problem_type == "PROGRAMMING"
            assert problem.contest_id == 1253
            assert problem.problemset_name is None
            assert problem.points == 500.0
            assert problem.rating == 1000
            assert problem.tags == ["implementation"]
    for statistic in problemset["problem_statistics"]:
        assert type(statistic.index) is str
        assert type(statistic.solved_count) is int
        assert type(statistic.contest_id) is int


def test_recent_status(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    status = api.problemset_recent_status(1)[0]
    assert type(status.id) is int
    assert type(status.creation_time_seconds) is int
    assert type(status.relative_time_seconds) is int
    assert type(status.problem) is Problem
    assert type(status.author) is Party
    assert type(status.programming_language) is str
    assert type(status.testset) is str
    assert type(status.passed_test_count) is int
    assert type(status.time_consumed_millis) is int
    assert type(status.memory_consumed_bytes) is int
    assert type(status.contest_id) is int
    assert status.verdict is None or type(status.verdict) is str
    assert status.points is None or type(status.points) is float


def test_recent_actions(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    action = api.recent_actions()[0]
    assert type(action.time_seconds) is int
    if hasattr(action, "blog_entry"):
        assert type(action.blog_entry) is BlogEntry
    if hasattr(action, "comment"):
        assert type(action.comment) is Comment


def test_user_blog_entries(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    entries = api.user_blog_entries("VadVergasov")
    for entry in entries:
        if entry.id == 74291:
            assert entry.author_handle == "VadVergasov"
            assert entry.original_locale == "ru"
            assert entry.id == 74291
            assert entry.title == "<p>Codeforces API python</p>"
            assert entry.allow_view_history == True
            assert entry.tags == [
                "#api",
                "api",
                "#codeforces",
                "#python",
                "#python 3",
                "python 3",
            ]
            assert entry.content is None


def test_user_friends(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    friends = api.user_friends()
    assert "aropan" in friends or "gepardo" in friends


def test_user_info(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    info = api.user_info(["VadVergasov", "tourist"])
    for user in info:
        assert user.email is None or type(user.email) is str
        assert user.open_id is None or type(user.open_id) is str
        assert user.first_name is None or type(user.first_name) is str
        assert user.last_name is None or type(user.last_name) is str
        assert user.country is None or type(user.country) is str
        assert user.vk_id is None or type(user.vk_id) is str
        assert user.country is None or type(user.country) is str
        assert user.city is None or type(user.city) is str
        assert user.organization is None or type(user.organization) is str
        assert type(user.contribution) is int
        assert user.rank is None or type(user.rank) is str
        assert user.rating is None or type(user.rating) is int
        assert user.max_rank is None or type(user.max_rank) is str
        assert user.max_rating is None or type(user.max_rating) is int
        assert type(user.last_online) is int
        assert type(user.registration_time_seconds) is int
        assert type(user.friend_of_count) is int
        assert type(user.avatar) is str
        assert type(user.title_photo) is str


def test_user_rated_list():
    api = CodeforcesApi()
    users = api.user_rated_list(True)
    for user in users:
        assert user.email is None or type(user.email) is str
        assert user.open_id is None or type(user.open_id) is str
        assert user.first_name is None or type(user.first_name) is str
        assert user.last_name is None or type(user.last_name) is str
        assert user.country is None or type(user.country) is str
        assert user.vk_id is None or type(user.vk_id) is str
        assert user.country is None or type(user.country) is str
        assert user.city is None or type(user.city) is str
        assert user.organization is None or type(user.organization) is str
        assert type(user.contribution) is int
        assert user.rank is None or type(user.rank) is str
        assert user.rating is None or type(user.rating) is int
        assert user.max_rank is None or type(user.max_rank) is str
        assert user.max_rating is None or type(user.max_rating) is int
        assert type(user.last_online) is int
        assert type(user.registration_time_seconds) is int
        assert type(user.friend_of_count) is int
        assert type(user.avatar) is str
        assert type(user.title_photo) is str


def test_user_rating():
    api = CodeforcesApi()
    ratings = api.user_rating("VadVergasov")
    for rating in ratings:
        assert type(rating.contest_id) is int
        assert type(rating.contest_name) is str
        assert type(rating.handle) is str
        assert type(rating.rank) is int
        assert type(rating.rating_update_time_seconds) is int
        assert type(rating.old_rating) is int
        assert type(rating.new_rating) is int


def test_user_status():
    api = CodeforcesApi()
    status = api.user_status("VadVergasov")
    for row in status:
        assert type(row.id) is int
        assert type(row.creation_time_seconds) is int
        assert type(row.relative_time_seconds) is int
        assert type(row.problem) is Problem
        assert type(row.author) is Party
        assert type(row.programming_language) is str
        assert type(row.testset) is str
        assert type(row.passed_test_count) is int
        assert type(row.time_consumed_millis) is int
        assert type(row.memory_consumed_bytes) is int
        assert row.contest_id is None or type(row.contest_id) is int
        assert row.verdict is None or type(row.verdict) is str
        assert row.points is None or type(row.points) is float
