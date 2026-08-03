class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if not len(nums):
            return 0
        dict1 = {}
        res = 1
        for i in nums:
            if i-1 in dict1:
                dict1[i] = dict1[i-1] + 1
                res = max(dict1[i], res)
            else:
                dict1[i] = 1
        return res
        