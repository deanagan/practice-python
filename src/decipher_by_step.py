from typing import List


def decipher_by_step(word: str, step: int) -> List[str]:
    '''
    Return substrings by step
    '''
    return [word[i::step] for i in range(step)]
