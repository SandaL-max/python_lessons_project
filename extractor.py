import re
import string

import nltk
from bs4 import BeautifulSoup
import pandas as pd

from raw_page import RawPage
from page_content import PageContent


class Extractor:
    @staticmethod
    def extract_sentences(raw_page: RawPage, page_content: PageContent):
        soup = BeautifulSoup(raw_page.data, "lxml")
        text = re.sub(
            r"\[.*?\]", "", "\n".join([x.get_text() for x in soup.find_all("p")])
        )
        page_content.sentences = pd.Series(nltk.tokenize.sent_tokenize(text))
        page_content.sentences.index.name = "Index"
        page_content.sentences.name = "Sentences"

    @staticmethod
    def extract_words(raw_page: RawPage, page_content: PageContent):
        soup = BeautifulSoup(raw_page.data, "lxml")
        text = (
            re.sub(
                r"\[.*?\]", "", "\n".join([x.get_text() for x in soup.find_all("p")])
            )
        ).lower()
        page_content.words = pd.Series(
            [x for x in nltk.word_tokenize(text) if x not in string.punctuation]
        )
        page_content.words.index.name = "Index"
        page_content.words.name = "Words"
