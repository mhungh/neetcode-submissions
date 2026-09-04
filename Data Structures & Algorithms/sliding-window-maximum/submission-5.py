import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []
        for i in range(k):
            h.append((-nums[i], i))

        heapq.heapify(h)
        res.append(-h[0][0])

        l = len(nums)
        for i in range(k, l):
            heapq.heappush(h, (-nums[i], i))
            pos = h[0][1]
            while pos <= (i-k):
                heapq.heappop(h)
                pos = h[0][1]
            res.append(-h[0][0])
        return res