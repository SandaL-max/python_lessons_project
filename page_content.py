class PageContent:
    def __init__(self):
        self.__sentences = None
        self.__words = None

    @property
    def sentences(self):
        return self.__sentences

    @sentences.setter
    def sentences(self, value):
        self.__sentences = value

    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, value):
        self.__words = value
