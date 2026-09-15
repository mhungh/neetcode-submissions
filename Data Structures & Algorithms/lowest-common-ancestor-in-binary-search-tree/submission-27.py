# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    



    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        h = [-1] * 105
        up = [[-1]*20 for _ in range(105)]

        h[root.val] = 0
        for i in range(9):
            up[root.val][i] = root

        def dfs(u):
            nodes = [u.left, u.right]
            for v in nodes:
                if v is None or v.val is None:
                    continue
                h[v.val] = h[u.val] + 1

                up[v.val][0] = u
                for i in range(1,10):
                    up[v.val][i] = up[up[v.val][i-1].val][i-1]

                
                dfs(v)
        dfs(root)
        if h[p.val] < h[q.val]:
            t = p
            p = q
            q = t

        k = h[p.val] - h[q.val]
        for i in range(0, 10):
            if k >> i & 1 : 
                p = up[p.val][i]
        
        if p.val == q.val:
            return p

        k = h[p.val].bit_length() - 1
        
        for i in range(k, -1, -1):
            if up[p.val][i] != up[q.val][i]:
                p = up[p.val][i]
                q = up[q.val][i]
        
        for i in range(0, 10):
            if up[0][i] == -1:
                print(-1)
            else:
                print(up[0][i].val)
        return up[p.val][0]
    