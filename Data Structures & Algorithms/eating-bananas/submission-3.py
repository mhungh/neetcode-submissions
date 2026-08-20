class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        res = max(piles)

        while left <= right:
            mid = left + (right-left) // 2
            total = 0
            for i in piles:
                total += math.ceil(i / mid)
            if total > h:
                left = mid + 1
            elif total <= h:
                res = min(res, mid)
                right = mid - 1

        
        return res
        
