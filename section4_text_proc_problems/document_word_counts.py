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
        self._fname = fname
        self._unique_words = sefl._compute_unique_words(fname)
        self._num_unique_words = len(self._unique_words)
        # TODO: Delete this comment and implement this function

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
        return unique_works
        # TODO: Delete this comment and implement this function

    def num_unique_words(self):
        '''
        Returns the number of unique words in this document.
        '''
        retun self._unique_words
        # TODO: Delete this comment and implement this function

    def get_fname(self):
        '''
        Returns the name of the document
        '''
        return self.fname
        # TODO: Delete this comment and implement this function
