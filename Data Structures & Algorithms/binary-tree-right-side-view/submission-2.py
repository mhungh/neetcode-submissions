# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root or root.val is None:
            return []

        res = []

        q = deque()
        q.append((root, 0))
        while q:
            curr = q.popleft()
            ptr = curr[0]
            idx = curr[1]

            if len(res) == idx:
                res.append([ptr.val])
            else:
                res[idx].append(ptr.val)

            if not ptr.left is None:
                q.append((ptr.left, idx+1))
            if not ptr.right is None:
                q.append((ptr.right, idx+1))  
        
        for i in range(len(res)):
            res[i] = res[i][-1]

        return res