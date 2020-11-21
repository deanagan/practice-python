from itertools import chain

def all_rows_can_match_word(puzzle, words):
    for row in puzzle:
        if ' ' in row:
            continue
        if not any(all(a==b or isinstance(a,int) for a,b in zip(row, word)) for word in words):
            return False
    return True

def all_columns_can_match_word(puzzle, words):
    columns = ([i[t] for i in puzzle] for t in range(len(puzzle[0])))
    for column in columns:
        if ' ' in column:
            continue
        if not any(all(a==b or isinstance(a,int) for a,b in zip(column, word)) for word in words):
            return False
    return True

def do_all_words_exist_in_puzzle(puzzle, words):

    if any(isinstance(e, int) for e in chain.from_iterable(puzzle)):
        return False

    # Read words by row
    found_words = [''.join(ch for ch in row if isinstance(ch, str)) for row in puzzle]
    # Read words by column
    found_words.extend([''.join([i[t] if isinstance(i[t], str) else '' for i in puzzle]) for t in range(len(puzzle[0]))])

    return all(word in found_words for word in words)

def replace_all(puzzle,/, dest, replacement):
    for row_number, row_elements in enumerate(puzzle):
        for column_number, value in enumerate(row_elements):
            if dest == value:
                puzzle[row_number][column_number] = replacement


def potential_solution(puzzle, words):
    return all_columns_can_match_word(puzzle, words) and all_rows_can_match_word(puzzle, words)


def solve(puzzle, words):

    if do_all_words_exist_in_puzzle(puzzle, words):
        return True

    if not potential_solution(puzzle, words):
        return False

    letters = (ch for ch in set(''.join(words)) if ch not in chain.from_iterable(puzzle))
    numbers = (num for num in chain.from_iterable(puzzle) if isinstance(num, int))

    for number in numbers:
        for letter in letters:

            replace_all(puzzle, number, letter)
            if potential_solution(puzzle, words) and solve(puzzle, words):
                return True
            else:
                replace_all(puzzle, letter, number) # backtrack
    return False


def cipher(puzzle, words):
    replace_all(puzzle, dest = 0, replacement=' ')
    return puzzle if solve(puzzle, words) else []

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
    print(result)

    expected = [['h', 'e', 'l', 'l', 'o'],
                ['a', ' ', 'e', ' ', 'z'],
                ['b', 'i', 'm', 'b', 'o'],
                ['i', ' ', 'm', ' ', 'n'],
                ['t', 'r', 'a', 'c', 'e']]

    #assert(result == expected)
