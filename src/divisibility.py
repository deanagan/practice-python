from itertools import permutations

# possibly faster version with memoization
def divisible_by_8(input: str) -> bool:
    cache = set()
    s = min(len(input), 3)
    for t in permutations(input, s):
        last3 = t[-3:]
        if last3 in cache:
            continue
        if int(''.join(last3)) % 8 == 0:
            return True

        cache.add(last3)

    return False

def divisible_by_8_oneliner(input: str) -> bool:
    return any(int(''.join(t)) % 8 == 0 for t in permutations(input, min(len(input),3)))
