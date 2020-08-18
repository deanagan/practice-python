from functools import cmp_to_key

def nearest_value(values: set, one: int) -> int:
    return sorted(values, key = cmp_to_key(lambda a,b: abs(a - one) - abs(b - one) or (a-b) ))[0]
    # Better
    # return min(values, key=lambda n: (abs(one - n), n))
