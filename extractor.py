import re

import nltk
from bs4 import BeautifulSoup

from raw_page import RawPage
from page_content import PageContent


class Extractor:
    @staticmethod
    def extract_sentences(raw_page: RawPage, page_content: PageContent):
        soup = BeautifulSoup(raw_page.data, "lxml")
        text = re.sub(
            r"\[.*?\]", "", "\n".join([x.get_text() for x in soup.find_all("p")])
        )
        result = nltk.tokenize.sent_tokenize(text)
        page_content.sentences = result

    @staticmethod
    def extract_words(raw_page: RawPage, page_content: PageContent):
        soup = BeautifulSoup(raw_page.data, "lxml")
        text = re.sub(
            r"\[.*?\]", "", "\n".join([x.get_text() for x in soup.find_all("p")])
        )
        result = nltk.word_tokenize(text)
        page_content.words = result
