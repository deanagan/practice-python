from itertools import combinations as comb

def non_repeat(line:str) -> str:
    all_unique = lambda word: len(set(word)) == len(word)
    words = {line[s:e]:0 for s,e in comb(range(len(line) + 1), r=2) if all_unique(line[s:e])}

    return max(words, key=len) if words else line


''' Algorithm:
1. Do single pass of characters in the string.
2. if character is a duplicate(already exists in the dict), get index of character after original. otherwise, retain current string index
3. record the index of current character.
4. record longest string's index if its distance from current index is longer than existing length. Otherwise, retain index.
5. store length of longest string.
6. do until single pass of string is completed.
'''

def non_repeat_single_pass(line: str) -> int:
    char_index = {}
    lsi, si, length = 0, 0, 0
    for i, ch in enumerate(line):
        si = max([char_index[ch] + 1, si]) if ch in char_index else si
        char_index[ch] = i
        lsi = si if i - si + 1 > length else lsi
        length = max([i - si + 1, length])

    return line[lsi:lsi+length]

if __name__ == '__main__':
    non_repeat_single_pass('abdjwawk')