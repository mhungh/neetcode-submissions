class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right = 0, l - 1
        smallest = 0
        if nums[left] <= nums[right]:
            pass
        else:
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] < nums[(mid+1)%l] and nums[mid] < nums[mid-1]:
                    smallest = mid
                    break
                elif nums[right] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        left, right = 0, l - 1
        while left <= right:
            mid = left + (right-left) // 2
            actual = (mid+smallest)%l
            if nums[actual] == target:
                return actual
            elif target < nums[actual]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1