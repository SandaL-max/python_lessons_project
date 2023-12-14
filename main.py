from bs4 import BeautifulSoup
import requests


class UrlError(Exception):
    def __init__(self, url):
        super().__init__(f"Invalid URL: {url}")
        self.url = url

    def __str__(self):
        return f"UrlError: Invalid URL - {self.url}"


class RawPage:
    def __init__(self, url):
        self.url = url
        self.__headline = None
        self.__data = None
        self.__test_data = None

    def __get_data(self):
        try:
            response = requests.get(self.url, timeout=100)
            soup = BeautifulSoup(response.text, "lxml")
            self.__headline = soup.title.string
            self.__data = soup.text
            self.__test_data = soup
        except requests.RequestException:
            raise UrlError(self.url)

    @property
    def data(self):
        if self.__data is None or self.__headline is None:
            self.__get_data()
        else:
            return self.__data

    @property
    def headline(self):
        if self.__data is None or self.__headline is None:
            self.__get_data()
        else:
            return self.__headline

    @property
    def test_data(self):
        self.__get_data()
        return self.__test_data


class PageContent:
    def __init__(self):
        self.__sentences = None
        self.__words = None

    @property
    def sentences(self):
        return self.__sentences

    @sentences.setter
    def sentences_setter(self, value):
        self.__sentences = value

    @property
    def words(self):
        return self.__words

    @words.setter
    def words_setter(self, value):
        self.__words = value


import re

delimiters = "\n", ". "
regex_pattern = "|".join(map(re.escape, delimiters))

test_page = RawPage("https://en.wikipedia.org/wiki/Python_(programming_language)")
result = test_page.test_data
new_text = [re.sub(r"\[.*?\]", "", x.get_text().strip()) for x in result.find_all("p")]

with open("results.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(new_text))
