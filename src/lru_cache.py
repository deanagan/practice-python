from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._usage = deque(maxlen=2)
        self._cache = {}

    def get(self, key: int) -> int:
        value = self._cache.get(key, -1)
        if value != -1:
            self._usage.append(key)

        return value

    def put(self, key: int, value: int) -> None:

        self._cache[key] = self._cache.get(key, value)
        if len(self._usage) >= self._capacity:
            least_key = self._usage.popleft()
            self._cache.pop(least_key)

        self._usage.append(key)
