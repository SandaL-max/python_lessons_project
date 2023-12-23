# Text Task Representation README

## Homework: Statistical Analysis of Wikipedia Article Texts

### Introduction

This project aims to conduct a linguistic analysis of Wikipedia articles focusing on vocabulary composition. The tasks involve creating classes to handle URL errors, downloading and parsing raw Wikipedia page content, extracting sentences and words, and performing statistical analytics on the text data.

### Task Breakdown

#### Task 0: Implementing UrlError Class (5 points)

- Create a class `UrlError` inherited from `Exception`.
- Implement `__init__` and `__str__` methods.
- Accepts a URL as an attribute.

#### Task 1: Creating RawPage Class (10 points)

- Develop a class named `RawPage` with attributes `url`, `data`, and `headline`.
- Constructor takes a Wikipedia article URL.
- Data is downloaded and stored in the `data` field.
- Headline is extracted and stored in the `headline` field.
- Raise `UrlError` for invalid URLs.
- Implement getters for `data` and `headline` using the `@property` decorator.

```python
class RawPage:
    def __init__(self, url):
        pass
```

#### Task 2: PageContent Class (5 points)

- Create a class `PageContent` with attributes `sentences` and `words`.
- Implement getters and setters for both attributes using the `@property` decorator.

```python
class PageContent:
    def __init__(self):
        pass
```

#### Task 3: Extractor Class (30 points)

- Develop a class named `Extractor`.
- Implement `extract_sentences` and `extract_words` methods.
- Make appropriate methods static.
- Extracts sentences and words from `RawPage` and stores them in `PageContent`.

```python
class Extractor:
    def __init__(self):
        pass

    @staticmethod
    def extract_sentences(raw_page: RawPage, page_content: PageContent):
        pass

    @staticmethod
    def extract_words(raw_page: RawPage, page_content: PageContent):
        pass
```

#### Task 4: PageAnalytics Class (30 points)

- Create a class `PageAnalytics` that takes a `PageContent` object as input.
- Implement `make_analytics` and `save_to_json` methods.
- Calculate and store various statistics.
- Provide a method to save statistics to a JSON file.
- Implement a clear representation for printing.

```python
class PageAnalytics:
    def __init__(self, page_content: PageContent):
        pass

    def make_analytics(self):
        pass

    def save_to_json(self, filename: str):
        pass

    def __str__(self):
        pass
```

#### Task 5: Comparative Analysis (5 points)

- Identify the article with the:
  - Longest sentence
  - Longest word
  - Most sentences
  - Most words

#### Task 6: Documentation (15 points)

- Enhance the program with docstrings.
- Describe the usage of libraries and functions in the class methods.
- Follow PEP 257 multi-line docstring guidelines.

### Refactoring

- Separate classes into different files.
- Move main functionality to `main.py`.
- Import necessary classes into `main.py`.

### Libraries

- Utilize `requests` for web scraping.
- Implement `bs4` for HTML parsing.
- Enhance analytics using `pandas` and `numpy` for data manipulation.

### Execution

Run the `main.py` file to perform the desired statistical analysis on selected Wikipedia articles.

### Conclusion

This project provides a structured approach to analyzing Wikipedia articles, offering a deeper understanding of their linguistic characteristics. It encourages modularity, code readability, and efficient use of libraries for statistical computations.

Project developed on Python 3.12.1
