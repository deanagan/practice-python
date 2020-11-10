

from itertools import takewhile as tw
def end_zeros(num: int) -> int:
    return sum(1 for _ in tw(lambda ch: ch == '0', str(num)[::-1]))

def beginning_zeros(number: str) -> int:
    return sum(1 for _ in tw(lambda n: n == '0', number))