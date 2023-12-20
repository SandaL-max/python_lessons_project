import json

import nltk

from raw_page import RawPage
from page_content import PageContent
from extractor import Extractor

nltk.download("punkt")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    raw_page = RawPage(url)
    page_content = PageContent()
    Extractor.extract_sentences(raw_page, page_content)
    Extractor.extract_words(raw_page, page_content)
    with open("sentences.json", "w", encoding="utf-8") as file:
        json.dump(page_content.sentences, file, indent=4)
    with open("words.json", "w", encoding="utf-8") as file:
        json.dump(page_content.words, file, indent=4)
