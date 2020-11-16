from heapq import heappush, heappop

def reverse_ascending(items):
    def pop_positives(subitems):
        yield from (-1 * heappop(subitems) for _ in range(len(subitems)))

    result, temp = [], []
    for i, n in enumerate(items):
        if temp and (-1*temp[0]) >= n:
            result.extend(pop_positives(temp))
        heappush(temp, -n)

    result.extend(pop_positives(temp))

    return result
