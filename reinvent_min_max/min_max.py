

def min_max(*args, **kwargs):
    k = kwargs.pop("key", lambda e: e)
    cmp = kwargs.pop("cmp", None)
    try:
        iargs = iter(*args)
        m = next(iargs)
    except TypeError:
        #not iterable
        iargs = args
        m = iargs[0]
    finally:
        for i in iargs:
            if cmp(k, i, m):
                m = i
        return m

def mymax(*args, **kwargs):
    kwargs['cmp'] = lambda k,i,m: k(i) > k(m)
    return min_max(*args, **kwargs)

def mymin(*args, **kwargs):
    kwargs['cmp'] = lambda k,i,m: k(i) < k(m)
    return min_max(*args, **kwargs)

if __name__ == "__main__":
    assert mymax(3, 2) == 3
    assert mymin(3, 2) == 2
    assert mymax([1, 2, 0, 3, 4]) == 4
    assert mymin("hello") == "e"
    assert mymax(2.2, 5.6, 5.9, key=int) == 5.6
    assert mymin([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]