


def mymin(*args, **kwargs):
    try:
        iterator = iter(*args)
        v = sorted(i for i in iterator)
        return v[0]

    except TypeError:
        #not iterable
        return sorted(args)[0]


def mymax(*args, **kwargs):
    k = kwargs.get("key", None)
    try:
        iterator = iter(*args)
        v = sorted(k(i) if k is not None else i for i in iterator)
        return v[-1]

    except TypeError:
        #not iterable
        v = sorted([i for i in args], key= lambda e: (k, args.index(e)*-1) if k is not None else e)
        return v[-1]


if __name__ == "__main__":
    assert mymax(3, 2) == 3
    assert mymin(3, 2) == 2
    assert mymax([1, 2, 0, 3, 4]) == 4
    assert mymin("hello") == "e"
    assert mymax(2.2, 5.6, 5.9, key=int) == 5.6
    # mymin([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]