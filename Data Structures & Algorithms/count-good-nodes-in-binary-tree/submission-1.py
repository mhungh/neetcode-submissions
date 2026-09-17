# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root or root.val is None:
            return []

        res = []
        ctr = 0

        q = deque()
        q.append((root, root.val))
        while q:
            curr = q.popleft()
            ptr = curr[0]
            mx = curr[1]

            if ptr.val >= mx:
                ctr += 1
                mx = ptr.val

            if not ptr.left is None:
                q.append((ptr.left, mx))
            if not ptr.right is None:
                q.append((ptr.right, mx))  
        
        return ctr