class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sumdict = {}
        for s in strs:
            curr = "".join(sorted(s))
            if curr in sumdict:
                sumdict[curr].append(s)
            else:
                sumdict[curr] = [s,]

        res = []
        for key, value in sumdict.items():
            res.append(value)
        return res