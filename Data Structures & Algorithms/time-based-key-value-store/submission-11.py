class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        right = len(self.d[key]) - 1
        left = 0
        curr = ""
        if right == 0 and self.d[key][0][0] <= timestamp:
            return self.d[key][0][1]
        while left < right:
            mid = left + (right-left+1) // 2
            if self.d[key][mid][0] <= timestamp:
                curr = self.d[key][mid][1]
                left = mid
            else:
                right = mid - 1
        if left == right and self.d[key][0][0] <= timestamp:
            return self.d[key][left][1]
        return curr
