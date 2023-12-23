from bs4 import BeautifulSoup
import requests

from url_error import UrlError


class RawPage:
    def __init__(self, url):
        self.url = url
        self.__headline = None
        self.__data = None
        self.__test_data = None

    def __get_data(self):
        """This method send get request on given url and store response

        Raises:
            UrlError: raises when something wrong with given url
        """
        try:
            response = requests.get(self.url, timeout=100)
            soup = BeautifulSoup(response.text, "lxml")
            self.__headline = soup.title.string
            self.__data = response.text
        except requests.RequestException:
            raise UrlError(self.url)

    @property
    def data(self):
        """Call __get_data if __data is None and return __data

        Returns:
            str: html text of requested url
        """
        if self.__data is None or self.__headline is None:
            self.__get_data()
        return self.__data

    @property
    def headline(self):
        """Call __get_data if __headline is None and return __headline

        Returns:
            str: headline of requested url
        """
        if self.__data is None or self.__headline is None:
            self.__get_data()
        return self.__headline
