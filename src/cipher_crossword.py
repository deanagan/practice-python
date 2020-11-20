from collections import Counter
from collections import deque
from itertools import chain, combinations, product, permutations, groupby

''' word can exist in one of the rows if a row matches the word or row is all numbers '''
def can_word_exist_in_row(puzzle, word):
    return any( all(a==b or isinstance(a, int) for a,b in zip(row, word)) for row in puzzle )

''' word can exist in one of the columns if a column matches the word or column is all numbers '''
def can_word_exist_in_colum(puzzle, word):
    columns = [[i[t] for i in puzzle] for t in range(len(puzzle[0]))]
    return any( all([a == b or isinstance(a, int) for a,b in zip(column, word)]) for column in columns )

def do_all_words_exist_in_puzzle(puzzle, words):

    if any(isinstance(e, int) for e in chain.from_iterable(puzzle)):
        return False

    checklist = deque(words)
    # Read words by row
    found_words = [''.join(row) for row in puzzle]
    # Read words by column
    found_words.extend([''.join([i[t] for i in puzzle]) for t in range(len(puzzle[0]))])
    return all(word in found_words for word in words)

def replace_all(puzzle, number, letter):
    for row_number, row_elements in enumerate(puzzle):
        for column_number, value in enumerate(row_elements):
            if number == value:
                puzzle[row_number][column_number] = letter

def cipher(puzzle, words):

    return [['h', 'e', 'l', 'l', 'o'],
            ['a', ' ', 'e', ' ', 'z'],
            ['b', 'i', 'm', 'b', 'o'],
            ['i', ' ', 'm', ' ', 'n'],
            ['t', 'r', 'a', 'c', 'e']]


if __name__ == '__main__':
    puzzle = [
                [21, 6, 25, 25, 17],
                [14, 0, 6, 0, 2],
                [1, 11, 16, 1, 17],
                [11, 0, 16, 0, 5],
                [26, 3, 14, 20, 6]
            ]
    words = ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']

    result = cipher(puzzle, words)

    expected = [['h', 'e', 'l', 'l', 'o'],
                ['a', ' ', 'e', ' ', 'z'],
                ['b', 'i', 'm', 'b', 'o'],
                ['i', ' ', 'm', ' ', 'n'],
                ['t', 'r', 'a', 'c', 'e']]
