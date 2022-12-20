import requests
import re
class DownloadHttpImage:
    def __init__(self, url):
        self._filename = re.search('\/(?=[^\/]*$).*', url).group(0).lstrip('/')
        self._url = url

    def download(self, path):
        with open(path + '/' + self._filename, 'wb') as f:
            f.write(requests.get(self._url).content)

        return self._filename