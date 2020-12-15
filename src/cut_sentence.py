


def cut_sentence(line: str, length: int) -> str:
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if len(line) <= length:
        return line

    return line[:max(0,line[:length+1].rfind(' '))] + '...'
