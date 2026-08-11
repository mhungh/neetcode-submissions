class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = []
        for i in range(len(position)):
            p.append([position[i],speed[i]])
        
        p = sorted(p, reverse=True)
        s = []
        for i in range(len(p)):
            l = len(s)
            time = (target - p[i][0]) / p[i][1]
            if l == 0 or s[l-1] < time:
                s.append(time)
        return len(s)
