from itertools import groupby

def is_stressful(subj: str):
    if subj.isupper() or subj.endswith("!!!"):
        return True
    filtered_subj = ''.join([i.lower() for i,_ in groupby(subj) if i.isalpha()])
    return any(red_word in filtered_subj for red_word in ("help", "asap", "urgent"))
