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
    urls = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/C_Sharp_(programming_language)",
        "https://en.wikipedia.org/wiki/JavaScript",
    ]
    pages = []
    for url in urls:
        raw_page = RawPage(url)
        page_content = PageContent()
        Extractor.extract_sentences(raw_page, page_content)
        Extractor.extract_words(raw_page, page_content)
        pages.append(PageAnalytics(page_content))
        pages[-1].make_analytics()
    sentences_len = np.array(
        [len(page.analytics_data["the_longest_sentence"]) for page in pages]
    )
    words_len = np.array(
        [len(page.analytics_data["top10_the_longest_words"][0]) for page in pages]
    )
    sentences_count = np.array(
        [page.analytics_data["sentences_count"] for page in pages]
    )
    words_count = np.array([page.analytics_data["words_count"] for page in pages])
    print(f"The longest sentence in {urls[sentences_len.argmax()]} arcticle")
    print(f"The longest word in {urls[words_len.argmax()]} arcticle")
    print(f"Most sentences in {urls[sentences_count.argmax()]} arcticle")
    print(f"Most words in {urls[words_count.argmax()]} arcticle")
