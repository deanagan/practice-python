import pytest

from src.cipher_crossword import cipher, entries_can_match_word

@pytest.mark.parametrize(('puzzle', 'words', 'expected'), [
    ([
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6]
    ],

    ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'],
    [['h', 'e', 'l', 'l', 'o'],
     ['a', ' ', 'e', ' ', 'z'],
     ['b', 'i', 'm', 'b', 'o'],
     ['i', ' ', 'm', ' ', 'n'],
     ['t', 'r', 'a', 'c', 'e']]),

    ([
        [14, 9, 24, 10, 14],
        [24, 0, 13, 0, 13],
        [13, 26, 13, 20, 18],
        [6, 0, 25, 0, 9],
        [14, 6, 9, 3, 14]
    ],
    ['sales', 'ovoid', 'loofa', 'stars', 'sodas', 'slots'],
    [['s', 'a', 'l', 'e', 's'],
     ['l', ' ', 'o', ' ', 'o'],
     ['o', 'v', 'o', 'i', 'd'],
     ['t', ' ', 'f', ' ', 'a'],
     ['s', 't', 'a', 'r', 's']]),

     ([
        [19, 23, 22, 1, 23],
        [8, 0, 9, 0, 6],
        [10, 1, 6, 2, 22],
        [13, 0, 8, 0, 18],
        [22, 21, 18, 13, 22]
    ],
    ['users', 'crime', 'eagle', 'eking', 'siege', 'uncle'],
    [['u', 's', 'e', 'r', 's'],
     ['n', ' ', 'k', ' ', 'i'],
     ['c', 'r', 'i', 'm', 'e'],
     ['l', ' ', 'n', ' ', 'g'],
     ['e', 'a', 'g', 'l', 'e']]),
])
def test_cipher_crossword(puzzle, words, expected):
    assert cipher(puzzle, words) == expected



@pytest.mark.parametrize(('puzzle, words, expected, note'), [
    (
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6]
        ], ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'], True, "All digits"
    ),
    (
        [
            ['h', 'e', 'l', 'l', 'o'],
            ['a', ' ', 'e', ' ', 'z'],
            ['b', 'i', 'm', 'b', 'o'],
            ['i', ' ', 'm', ' ', 'n'],
            ['t', 'r', 'a', 'c', 'e']
        ], ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'], True, "Has all words in row"
    ),
    (
        [
            [32, 'e', 'l', 'l', 2],
            ['a', ' ', 'e', ' ', 'z'],
            ['b', 'i', 'm', 'b', 'o'],
            ['i', ' ', 'm', ' ', 'n'],
            ['t', 9, 'a', 7, 'e']
        ], ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'], True, "Mix of words and digits"
    ),
    (
        [
            [32, 'e', 's', 'l', 2],
            ['a', ' ', 'e', ' ', 'z'],
            ['b', 'i', 'm', 'b', 'o'],
            ['i', ' ', 'm', ' ', 'n'],
            ['t', 9, 'a', 7, 'e']
        ], ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace'], False, "Mix of words and digits"
    ),

])
def test_any_entry_can_match_word(puzzle, words, expected, note):
    assert entries_can_match_word(puzzle, words, puzzle) == expected, note
