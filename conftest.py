import pytest
import os
from config.config import load_config
from utils.http_client import HTTPClient
from services.posts_service import PostsService
from services.comments_service import CommentsService
from consts import urls


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='env to run tests against (dev/prod)')


@pytest.fixture(scope='session')
def config(request):
    env = request.config.getoption('--env')
    cfg = load_config(env)
    # set config into urls module so other modules can read hostname
    urls.set_config(cfg)
    return cfg


@pytest.fixture(scope='session')
def http_client():
    return HTTPClient()


@pytest.fixture(scope='session')
def posts_service(http_client, config):   
    return PostsService(http_client)


@pytest.fixture(scope='session')
def comments_service(http_client, config):  
    return CommentsService(http_client)