"""
Config file for tests
"""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--api_key",
        action="store",
        default="api_key",
        help="API key for tests",
    )
    parser.addoption(
        "--api_secret",
        action="store",
        default="api_secret",
        help="API secret for tests",
    )


@pytest.fixture
def api_key(request):
    return request.config.getoption("--api_key")


@pytest.fixture
def api_secret(request):
    return request.config.getoption("--api_secret")
