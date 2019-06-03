# This program prints the documents in a directory ordered
# by the number of unique words.

from directory_word_counts import DirectoryWordCounts


def main():

    directories = input('Please enter a directory: ')
    print(directories)

    print('Building DirectoryWordCounts')
    print()
    dwc = DirectoryWordCounts.DirectoryWordCounts(directories)
    ranking = dwc.uniqueness_list()
    for r in ranking:
        print(r)


if __name__ == '__main__':
    main()
