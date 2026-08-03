class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        mx = 0
        curr = s[0]
        res = 0
        dct = {}
        for r in range(len(s)):
            if s[r] not in dct:
                dct[s[r]] = 0
            dct[s[r]] += 1
            if dct[s[r]] >= dct[curr]:
                curr = s[r]
                mx = dct[s[r]]
            
            while (r-l+1) - mx > k:
                dct[s[l]] = max(dct[s[l]]-1, 0)
                l += 1

            res = max(res, r - l + 1)
            
        return res
