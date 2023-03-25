class AllOne:

    def __init__(self):
        self._keys = {}
        self._counts = [True]
        self._min_count = 1
        self._max_count = 0

    def inc(self, key):
        if key not in self._keys:
            self._keys[key] = 1
            self._min_count = min(self._min_count, 1)
        else:
            self._counts[self._keys[key]].remove(key)
            self._keys[key] += 1
        count = self._keys[key]
        if count >= len(self._counts):
            self._counts.append(set())
        self._counts[count].add(key)
        self._max_count = max(self._max_count, count)

    def dec(self, key):
        if key not in self._keys:
            raise Exception()
        else:
            self._counts[self._keys[key]].remove(key)
            self._keys[key] -= 1
        count = self._keys[key]
        if count > 0:
            self._counts[count].add(key)
            self._min_count = min(self._min_count, count)
        else:
            del self._keys[key]

    def getMaxKey(self):
        while not self._counts[self._max_count]:
            # amortized O(1) across calls to inc and dec
            self._max_count -= 1
        if self._max_count == 0:
            return ""
        return next(iter(self._counts[self._max_count]))

    def getMinKey(self):
        while self._min_count < len(self._counts) and not self._counts[self._min_count]:
            # amortized O(1) across calls to inc and dec
            self._min_count += 1
        if self._min_count == len(self._counts):
            return ""
        return next(iter(self._counts[self._min_count]))
