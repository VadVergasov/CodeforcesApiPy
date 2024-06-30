"""
Testing requests to api with auth.
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
    assert blog_entry.allow_view_history
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
            assert not hack.hacker.ghost
            assert hack.hacker.members[0].handle == "VietCT"
            assert hack.hacker.team_id is None
            assert hack.hacker.contest_id == 1311
            assert hack.hacker.room is None
            assert hack.hacker.start_time_seconds == 1582554900
            assert hack.defender.members[0].handle == "UMR"
            assert hack.defender.participant_type == "OUT_OF_COMPETITION"
            assert not hack.defender.ghost
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


def test_contest_list(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    contests = api.contest_list()
    for contest in contests:
        if contest.id == 1496:
            assert contest.name == "Codeforces Round 706 (Div. 2)"
            assert contest.contest_type == "CF"
            assert contest.phase == "FINISHED"
            assert not contest.frozen
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
            assert change.contest_name == "Codeforces Round 622 (Div. 2)"
            assert change.rank == 2303
            assert change.rating_update_time_seconds == 1582455900
            assert change.old_rating == 1330
            assert change.new_rating == 1381
            break


def test_contest_standings(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    standings = api.contest_standings(1313, handles=["VadVergasov"])
    assert standings["contest"].id == 1313
    assert standings["contest"].name == "Codeforces Round 622 (Div. 2)"
    assert standings["contest"].contest_type == "CF"
    assert standings["contest"].phase == "FINISHED"
    assert not standings["contest"].frozen
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
            assert not row.party.ghost
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


def test_contest_status(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
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
            assert not row.author.ghost
            assert row.author.team_id is None
            assert row.author.contest_id == 1313
            assert row.author.room == 10
            assert row.author.start_time_seconds == 1582448700
            assert row.programming_language == "C++17 (GCC 7-32)"
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
        assert isinstance(statistic.index, str)
        assert isinstance(statistic.solved_count, int)
        assert isinstance(statistic.contest_id, int)


def test_recent_status(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    status = api.problemset_recent_status(1)[0]
    assert isinstance(status.id, int)
    assert isinstance(status.creation_time_seconds, int)
    assert isinstance(status.relative_time_seconds, int)
    assert isinstance(status.problem, Problem)
    assert isinstance(status.author, Party)
    assert isinstance(status.programming_language, str)
    assert isinstance(status.testset, str)
    assert isinstance(status.passed_test_count, int)
    assert isinstance(status.time_consumed_millis, int)
    assert isinstance(status.memory_consumed_bytes, int)
    assert isinstance(status.contest_id, int)
    assert status.verdict is None or isinstance(status.verdict, str)
    assert status.points is None or isinstance(status.points, float)


def test_recent_actions(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    action = api.recent_actions()[0]
    assert isinstance(action.time_seconds, int)
    if hasattr(action, "blog_entry"):
        assert isinstance(action.blog_entry, BlogEntry)
    if hasattr(action, "comment"):
        assert isinstance(action.comment, Comment)


def test_user_blog_entries(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    entries = api.user_blog_entries("VadVergasov")
    for entry in entries:
        if entry.id == 74291:
            assert entry.author_handle == "VadVergasov"
            assert entry.original_locale == "ru"
            assert entry.id == 74291
            assert entry.title == "<p>Codeforces API python</p>"
            assert entry.allow_view_history
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


def test_user_info(api_key, api_secret, check_user):
    api = CodeforcesApi(api_key, api_secret)
    info = api.user_info(["VadVergasov", "tourist"])
    for user in info:
        check_user(user)


def test_user_rated_list(api_key, api_secret, check_user):
    api = CodeforcesApi(api_key, api_secret)
    users = api.user_rated_list(True)
    for user in users:
        check_user(user)


def test_user_rating(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    ratings = api.user_rating("VadVergasov")
    for rating in ratings:
        assert isinstance(rating.contest_id, int)
        assert isinstance(rating.contest_name, str)
        assert isinstance(rating.handle, str)
        assert isinstance(rating.rank, int)
        assert isinstance(rating.rating_update_time_seconds, int)
        assert isinstance(rating.old_rating, int)
        assert isinstance(rating.new_rating, int)


def test_user_status(api_key, api_secret):
    api = CodeforcesApi(api_key, api_secret)
    status = api.user_status("VadVergasov")
    for row in status:
        assert isinstance(row.id, int)
        assert isinstance(row.creation_time_seconds, int)
        assert isinstance(row.relative_time_seconds, int)
        assert isinstance(row.problem, Problem)
        assert isinstance(row.author, Party)
        assert isinstance(row.programming_language, str)
        assert isinstance(row.testset, str)
        assert isinstance(row.passed_test_count, int)
        assert isinstance(row.time_consumed_millis, int)
        assert isinstance(row.memory_consumed_bytes, int)
        assert row.contest_id is None or isinstance(row.contest_id, int)
        assert row.verdict is None or isinstance(row.verdict, str)
        assert row.points is None or isinstance(row.points, float)
