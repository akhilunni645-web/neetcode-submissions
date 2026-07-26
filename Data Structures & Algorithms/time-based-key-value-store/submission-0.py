
class TimeMap:

    def __init__(self):
        # Dictionary:
        # key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        # Create list if key doesn't exist
        if key not in self.store:
            self.store[key] = []

        # Append (timestamp, value)
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        # Key not found
        if key not in self.store:
            return ""

        values = self.store[key]

        l = 0
        r = len(values) - 1

        res = ""

        while l <= r:

            mid = (l + r) // 2

            # Current timestamp <= target
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1      # Search for a later valid timestamp
            else:
                r = mid - 1      # Search left side

        return res