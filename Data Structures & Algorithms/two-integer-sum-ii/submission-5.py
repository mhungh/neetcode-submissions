class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1 
        sm = numbers[l] + numbers[r]
        while True:
            sm = numbers[l] + numbers[r]
            if sm == target:
                return [l+1,r+1]
            elif sm < target:
                l = l+1
            elif sm > target:
                r = r-1