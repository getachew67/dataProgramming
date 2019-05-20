# 1664741

import math
import os
import re
from document import Document


class SearchEngine:
    """
    The SearchEngine class contains information of the documents on the
    directory and searches the related documents
    """
    def __init__(self, dir):
        """
        Constructs a new SearchEngine object with the given directory name.
        It contains set of the documents, set of all words, inverse
        index, and the dictionary of word: IDF of the word.
        """
        self._dname = dir
        self._docs = set()
        for file in os.listdir(dir):
            doc = Document(dir + '/' + file)
            self._docs.add(doc)
        self._all_words = self._get_all_words()
        self._inverse_index = self._get_inverse_index()
        self._word_idf = dict()
        for word in self._all_words:
            self._word_idf[word] = self._calculate_idf(word)

    def _get_all_words(self):
        """
        Returns the set of all words appeared in all documents
        """
        words_set = set()
        for doc in self._docs:
            for word in doc.get_words():
                words_set.add(word)
        return words_set

    def _get_inverse_index(self):
        """
        Returns the dictionary of word: list of documents containing the word
        """
        ii = dict()
        for word in self._all_words:
            doc_list = list()
            for doc in self._docs:
                if word in doc.get_words():
                    doc_list.append(doc)
            ii[word] = doc_list
        return ii

    def _calculate_idf(self, term):
        """
        Returns IDF of the given term
        """
        if term not in self._all_words:
            return 0
        total = len(self._docs)
        num = len(self._inverse_index.get(term))
        return math.log(total/num)

    def get_word_idf(self, term):
        """
        Returns the IDF of the given term
        """
        if term not in self._all_words:
            return 0
        else:
            return self._word_idf[term]

    def search(self, string):
        """
        Returns the list of documents names.
        The list is sorted in descending order of TF-IDF.
        """
        doc_tfidf = list()
        words = string.split()
        wList = list()
        for word in words:
            word = word.lower()
            word = re.sub(r'\W+', '', word)
            wList.append(word)
        count = 0
        for w in wList:
            if w in self._all_words:
                count += 1
        if count == 0:
            return None
        else:
            for doc in self._docs:
                score = 0
                for word in wList:
                    if word in doc.get_words():
                        score += doc.term_frequency(word)*self._word_idf[word]
                if score != 0:
                    doc_tfidf.append((doc.get_fname(), score))
            sorted_list = sorted(doc_tfidf, key=lambda f: f[1], reverse=True)
            return [t[0] for t in sorted_list]

    def get_dname(self):
        """
        Returns the directory name
        """
        return self._dname
