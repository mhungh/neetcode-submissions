class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        a = []
        for i in range(len(s)):
            if s[i] not in a:
                a.append(s[i])
            else:
                res = max(res, len(a))
                while(s[l] != s[i]):
                    
                    a.remove(s[l])
                    l += 1
                l += 1
        res = max(res, len(a))
        return res
                
                
