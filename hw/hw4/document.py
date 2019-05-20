# 1664741

import re


class Document:
    """
    The Document class represents a document and contains
    the methods of calculating term frequency of the word
    and the unique words in the document.
    """
    def __init__(self, fname):
        """
        Initializes a new Document object. The fname is the name of the file.
        The dictionary of word keys and count values and the list of the
        unique words will be stored.
        """
        self._fname = fname
        self._word_count_dict = self._compute_word_count_dict(fname)
        self._words = list(self._word_count_dict.keys())

    def _compute_word_count_dict(self, fname):
        """
        Returns a dictionary of word:count
        """
        wordCountDict = dict()
        with open(fname) as f:
            tokens = f.read().split()
            # lines = f.readlines()
            # for line in lines:
            # tokens = line.split()
            for token in tokens:
                token = token.lower()
                token = re.sub(r'\W+', '', token)
                if token not in wordCountDict:
                    wordCountDict[token] = 1
                else:
                    wordCountDict[token] += 1
        return wordCountDict

    def term_frequency(self, term):
        """
        Returns the frequency of the given term in the document.
        It is case-insentive and removes punctuation from the given term.
        If the given term doesn't exist in the document, return 0.
        """
        if term not in self.get_words():
            return 0
        total = sum(self._word_count_dict.values())
        count = self._word_count_dict[term]
        return count/total

    def get_words(self):
        """
        Returns the list of all the words appeared in the document.
        """
        return self._words

    def get_fname(self):
        """
        Returns the name of the file.
        """
        return self._fname
