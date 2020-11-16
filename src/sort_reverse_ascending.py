from heapq import heappush, heappop

def reverse_ascending(items):
    def pop_positives(subitems):
        yield from (abs(heappop(subitems)) for _ in range(len(subitems)))

    result, temp = [], []
    for n in items:
        if temp and abs(temp[0]) >= n:
            result.extend(pop_positives(temp))
        heappush(temp, -n)

    result.extend(pop_positives(temp))

    return result
