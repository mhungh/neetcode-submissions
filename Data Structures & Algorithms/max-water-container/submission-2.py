class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            h = min(heights[left], heights[right])
            t = h*(right-left)
            res = max(t,res)
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        return res