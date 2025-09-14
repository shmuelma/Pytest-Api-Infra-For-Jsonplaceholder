import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class HTTPClient:
    def __init__(self, timeout=10):
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500,502,503,504])
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.timeout = timeout


    def get(self, url, params=None, **kwargs):
        resp = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
        resp.raise_for_status()
        return resp.json()