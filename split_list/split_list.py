from itertools import zip_longest

def split_list(items: list) -> list:
    l = len(items) + (0 if len(items) % 2 == 0 else 1)
    result = [[e for e in v if e is not None] for v in zip_longest(*[iter(items)]* (l // 2))]
    if len(result) == 1:
        result.append([])
    elif len(result) == 0:
        result.extend([[],[]])
    return result

if __name__ == "__main__":
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
