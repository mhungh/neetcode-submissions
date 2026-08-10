class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        l = len(temperatures) -1
        t = [0]*(l+1)
        for i in range(l-1, -1, -1):
            j = i+1
            while j <= l and temperatures[j] <= temperatures[i]:
                if t[j] == 0:
                    j = l+1
                    break
                j += t[j]
            if j <= l:
                t[i] = j - i
        
        return t
            

            