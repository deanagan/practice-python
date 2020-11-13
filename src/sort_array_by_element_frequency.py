

def frequency_sort(items):
    return sorted(items, key=lambda e: (items.count(e), len(items) - items.index(e)), reverse=True)

''' sort in frequency first, then ascending '''
def asc_frequency_sort(items):
    return sorted(items, key=lambda e: (items.count(e), -e), reverse=True)


if __name__ == '__main__':
    v = asc_frequency_sort([3, 4, 11, 13, 11, 4, 4, 7, 3])
    print(v, '== [4, 4, 4, 3, 3, 11, 11, 7, 13]')
