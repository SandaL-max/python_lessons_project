import json

import nltk
import numpy as np
import pandas as pd

from raw_page import RawPage
from page_content import PageContent
from extractor import Extractor
from page_analytics import PageAnalytics

# nltk.download("punkt")
# nltk.download("stopwords")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    raw_page = RawPage(url)
    page_content = PageContent()
    Extractor.extract_sentences(raw_page, page_content)
    Extractor.extract_words(raw_page, page_content)
    page_content.sentences.to_csv("output/sentences.csv")
    page_content.words.to_csv("output/words.csv")
    page_analytics = PageAnalytics(page_content)
    page_analytics.make_analytics()
