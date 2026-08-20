class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        left, right = 0, l - 1
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[(mid+1)%l] and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[right] > nums[mid]:
                right = mid - 1
            elif nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1