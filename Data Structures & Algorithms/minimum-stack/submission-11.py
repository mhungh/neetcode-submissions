class MinStack:
    def __init__(self):
        self.s = []
        self.mn = float('inf')

    def push(self, val: int) -> None:
        if self.mn == "#":
            self.s.append(0)
            self.mn = val
        else:
            self.s.append(val - self.mn)
            if val < self.mn:
                self.mn = val

    def pop(self) -> None:
        if not self.s:
            return
        
        p = self.s.pop()
        if p <= 0:
            self.mn -= p


    def top(self) -> int:
        if not self.s:
            return

        t = self.s[len(self.s)-1]
        if t > 0:
            return t + self.mn
        else:
            return self.mn

    def getMin(self) -> int:
        if not self.s:
            return
        return self.mn