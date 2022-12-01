"""
Config file for tests
"""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--api_key",
        action="store",
        default="",
        help="API key for tests",
    )
    parser.addoption(
        "--api_secret",
        action="store",
        default="",
        help="API secret for tests",
    )


@pytest.fixture
def api_key(request):
    try:
        import conf

        return conf.api_key
    except FileNotFoundError:
        return request.config.getoption("--api_key")


@pytest.fixture
def api_secret(request):
    try:
        import conf

        return conf.api_secret
    except FileNotFoundError:
        return request.config.getoption("--api_secret")


@pytest.fixture
def check_user():
    def check(user):
        assert user.email is None or isinstance(user.email, str)
        assert user.open_id is None or isinstance(user.open_id, str)
        assert user.first_name is None or isinstance(user.first_name, str)
        assert user.last_name is None or isinstance(user.last_name, str)
        assert user.country is None or isinstance(user.country, str)
        assert user.vk_id is None or isinstance(user.vk_id, str)
        assert user.country is None or isinstance(user.country, str)
        assert user.city is None or isinstance(user.city, str)
        assert user.organization is None or isinstance(user.organization, str)
        assert isinstance(user.contribution, int)
        assert user.rank is None or isinstance(user.rank, str)
        assert user.rating is None or isinstance(user.rating, int)
        assert user.max_rank is None or isinstance(user.max_rank, str)
        assert user.max_rating is None or isinstance(user.max_rating, int)
        assert isinstance(user.last_online, int)
        assert isinstance(user.registration_time_seconds, int)
        assert isinstance(user.friend_of_count, int)
        assert isinstance(user.avatar, str)
        assert isinstance(user.title_photo, str)

    return check
