class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = {}
        
        for i in t:
            d1[i] = 1 + d1.get(i, 0)

        tot = len(d1)
        curr = 0

        mn = len(s) + 1
        res = ""
        l = 0
        d2 = {}
        for r in range(len(s)):
            if s[r] in t:
                d2[s[r]] = 1 + d2.get(s[r], 0)
                if d2[s[r]] == d1[s[r]]:
                    curr += 1
                
                while curr == tot:
                    if s[l] in t:
                        if mn > r-l+1:
                            mn = r-l+1
                            res = s[l:r+1]
                        if d2[s[l]] == d1[s[l]]:
                            curr -= 1
                        d2[s[l]] -= 1
                    l += 1
                    

                

        return res
        
        

                    

        
            