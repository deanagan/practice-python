
def even_last(array):
    """
        sums even-indexes elements and multiply at the last
    """
    return (sum([val for i,val in enumerate(array) if i % 2 == 0]) * array[-1] if array else 0)