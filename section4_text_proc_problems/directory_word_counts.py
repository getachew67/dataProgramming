import os
from document_word_counts import DocumentWordCounts


class DirectoryWordCounts:
    '''
    The DirectoryWordCounts contains information
    on the unique word counts for multiple files.
    '''

    def __init__(self, dir):
        '''
        Constructs a new DirectoryWordCounts object given a directory name.
        '''
        self._docs = set()
        for file in os.listdir(dir):
            doc = DocumentWordCounts(dir + '/' + file)
            self._docs.add(doc)
        # TODO: Delete this comment and implement this function

    def uniqueness_list(self):
        '''
        Returns a list of the documents in this DirectoryWordCounts as tuples
        (document name, number of unique words) sorted in descending order by
        number of unique words.

        Ie. if DirectoryWordCounts has “a.txt” with 1 unique word and
        “b.txt” with 25 unique words, the list returned should be:
        [(“b.txt”, 25), (“a.txt”, 1)]
        '''
        doc_list = list(self._docs)
        sorted_list = sorted(doc_list, key=lambda doc:doc.num_unique_words(), reverse = True)
        return [(doc.get_fname(), doc.num_unique_words()) for doc in sorted_list]

        # TODO: Delete this comment and implement this function and delete
        # the return statement
        return []
