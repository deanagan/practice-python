
'''
 You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.

Some possible cases:

    Filename cannot be an empty string;
    Files without the extension should go before the files with one;
    Filename ".config" has an empty extension and a name ".config";
    Filename "config." has an empty extension and a name "config.";
    Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
    Filename ".imp.xls" has an extension "xls" and a name ".imp".

Input: A list of filenames.

Output: A list of filenames.
'''
from typing import List
def sort_by_ext(filenames: List[str]) -> List[str]:
    by_no_extension = lambda word: 0 if word.endswith('.') else word[1:-1].count('.')
    by_ext_name = lambda word: word[word.rindex('.') + 1:] or word

    return sorted(filenames, key = lambda word: (by_no_extension(word), by_ext_name(word), word))
