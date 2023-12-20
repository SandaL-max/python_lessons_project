class UrlError(Exception):
    def __init__(self, url):
        super().__init__(f"Invalid URL: {url}")
        self.url = url

    def __str__(self):
        return f"UrlError: Invalid URL - {self.url}"
