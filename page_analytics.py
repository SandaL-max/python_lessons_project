# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
import os.path
import json

import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from page_content import PageContent


class PageAnalytics:
    def __init__(self, page_content: PageContent):
        self.url = page_content.url
        self.sentences = page_content.sentences
        self.words = page_content.words
        self.analytics_data = None

    def make_analytics(self):
        """Generate analytics for the given Wikipedia article.

        The analytics include the following:
        1) Top 10 most frequent words.
        2) Top 10 most frequent words without stop words.
        3) Mean and median word lengths.
        4) Top 10 longest words.
        5) Mean and median sentence lengths.
        6) The longest sentence.
        7) Count of sentences.
        8) Count of words.

        Updates the 'analytics_data' attribute with the computed statistics.
        """
        self.analytics_data = {"url": self.url}
        # Количество слов
        words_count = (
            self.words.groupby(self.words).count().sort_values(ascending=False)
        )
        self.analytics_data["top10_the_most_frequent_words"] = words_count.head(
            10
        ).index.values.tolist()

        # Количество слов без предлогов и союзов
        stop_words = list(stopwords.words("english"))
        words_count_without_stop_words = (
            (self.words[~self.words.isin(stop_words)])
            .groupby(self.words)
            .count()
            .sort_values(ascending=False)
        )
        self.analytics_data[
            "top10_the_most_frequent_words_without_stop_words"
        ] = words_count_without_stop_words.head(10).index.values.tolist()

        # Самые длинные слова
        words_len = pd.DataFrame(
            {"Words": self.words, "Words length": self.words.str.len()}
        )
        words_len = words_len.drop_duplicates("Words").sort_values(
            "Words length", ascending=False
        )
        self.analytics_data["top10_the_longest_words"] = words_len.head(10)[
            "Words"
        ].tolist()

        # Средняя и медианная длина слова
        self.analytics_data["mean_words_len"] = words_len["Words length"].mean()
        self.analytics_data["median_words_len"] = words_len["Words length"].median()

        # Самое длинное предложение
        sentences_len = pd.DataFrame(
            {"Sentences": self.sentences, "Sentences length": self.sentences.str.len()}
        ).sort_values("Sentences length", ascending=False)
        self.analytics_data["the_longest_sentence"] = sentences_len.head(1)[
            "Sentences"
        ].tolist()[0]

        # Средняя и медианная длина предложения
        self.analytics_data["mean_sentences_len"] = sentences_len[
            "Sentences length"
        ].mean()
        self.analytics_data["median_sentences_len"] = sentences_len[
            "Sentences length"
        ].median()

        # Сколько слов и предложений
        self.analytics_data["words_count"] = self.words.size
        self.analytics_data["sentences_count"] = self.sentences.size

    def save_to_json(self, filename: str = "output/analyses.json"):
        """Stores analytics to json file

        Args:
            filename (str, optional): path json file where should'be stored analytics. Defaults to "output/analyses.json".
        """
        analysed = []
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as file:
                analysed = json.load(file)
        if self.analytics_data is None:
            self.make_analytics()
        analysed.append(self.analytics_data)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(analysed, file, indent=4)

    def __str__(self):
        if self.analytics_data is None:
            self.make_analytics()
        return json.dumps(self.analytics_data, indent=4)
