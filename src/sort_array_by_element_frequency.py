

def frequency_sort(items):
    return sorted(items, key=lambda e: (items.count(e), len(items) - items.index(e)), reverse=True)
