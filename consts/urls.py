from config.config import load_config

# reads hostname from loaded config in conftest


_CONFIG = None

def set_config(config):
    global _CONFIG
    _CONFIG = config


def posts_url(path: str = 'posts') -> str:
    assert _CONFIG is not None, "Config not set. call set_config() from conftest"
    return f"{_CONFIG.HOSTNAME.rstrip('/')}/{path.lstrip('/')}"


def comments_url(path: str = 'comments') -> str:
    assert _CONFIG is not None, "Config not set. call set_config() from conftest"
    return f"{_CONFIG.HOSTNAME.rstrip('/')}/{path.lstrip('/')}"