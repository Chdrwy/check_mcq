import requests

class DownloadHttpImage:
    def __init__(self, url):
        self._url = url

    def download(self, path):
        with open(path, 'wb') as f:
            f.write(requests.get(self._url).content)