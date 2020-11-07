from itertools import zip_longest

def split_pairs(a, grp_size = 2):
    return (''.join(i) for i in zip_longest(*[iter(a)] * grp_size, fillvalue='_'))