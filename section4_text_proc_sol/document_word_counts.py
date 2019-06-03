# Defines a class to count the words in a single document

import re


class DocumentWordCounts:
    '''
    The DocumentWordCounts class represents a document and contains methods
    related to the unique words in this document. Uniqueness is
    case-insensitive and ignores punctuation and non-alphabetic characters.
    (ie. “hello” and “HeLo!?!” are considered the same word.)
    '''

    def __init__(self, fname):
        '''
        Initializes a new DocumentWordCounts object. The fname is the name of
        the file this DocumentWordCounts will represent. You will store all
        words in the unique words in a set.
        '''
        # the unique_words field is a set that contains all unique words that
        # are in the file
        self._unique_words = self._compute_unique_words(fname)
        self._fname = fname
        self._num_unique_words = len(self._unique_words)

    def _compute_unique_words(self, fname):
        '''
        Returns a set of all of the words in the file called fname.
        Uniqueness is case-insensitive and ignores punctuation and
        non-alphabetic characters. (ie. “hello” and “HeLo!?!” are
        considered the same word.)
        '''
        unique_words = set()
        with open(fname) as f:
            tokens = f.read().split()
            for token in tokens:
                token = token.lower()
                token = re.sub(r'\W+', '', token)
                unique_words.add(token)
        return unique_words

    def num_unique_words(self):
        '''
        Returns the number of unique words in this document.
        '''
        return self._num_unique_words

    def get_fname(self):
        '''
        Returns the name of the document
        '''
        return self._fname
