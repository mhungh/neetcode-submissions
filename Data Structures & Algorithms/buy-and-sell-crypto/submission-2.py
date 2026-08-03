class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0
        n = len(prices)
        for i in range(n):
            low = min(low, prices[i])
            res = max(res, prices[i]-low)
        return res
