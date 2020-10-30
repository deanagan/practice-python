


def second_index(text: str, symbol: str) -> [int, None]:
    return [i for i,ch in enumerate(text) if ch ==symbol][1] if text.count(symbol) > 1 else None
