class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        lefts = [-1]*l
        rights = [-1]*l
        s1, s2 = [], []
        for i in range(l):
            while len(s2) != 0 and heights[s2[-1]] >= heights[i]:
                s2.pop()

            tl = len(s2)
            if tl != 0:
                lefts[i] = s2[-1]
            
            s2.append(i)

            while len(s1) != 0 and heights[s1[-1]] >= heights[l-1-i]:
                s1.pop()

            tl = len(s1)
            if tl != 0:
                rights[l-1-i] = s1[-1]
            
            s1.append(l-1-i)
        res = 0
        for i in range(l):
            lt, rt = lefts[i], rights[i]
            if rights[i] == -1:
                rt = l
            if lefts[i] == -1:
                lt = -1 
            res = max(res, (rt - lt - 1)* heights[i])
        return res
            
