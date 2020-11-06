from itertools import takewhile as tw
def end_zeros(num: int) -> int:
    return sum(1 for _ in tw(lambda ch: ch == '0', str(num)[::-1]))