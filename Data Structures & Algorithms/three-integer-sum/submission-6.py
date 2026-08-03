class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        l = len(nums)
        for i in range(l):
            a = nums[i]
            if a > 0 or (i>0 and a == nums[i-1]):
                continue
            left = i+1
            right = l-1
            while left < right:
                sm = a + nums[left] + nums[right]
                if sm == 0:
                    if [a,nums[left],nums[right]] not in res:
                        res.append([a,nums[left],nums[right]])
                    left = left+1
                elif sm < 0 :
                    left = left + 1
                elif sm > 0:
                    right = right -1
        return res 