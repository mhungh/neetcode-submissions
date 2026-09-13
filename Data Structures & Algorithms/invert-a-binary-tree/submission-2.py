# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        
        l, r = None, None
        if root.left:
            self.invertTree(root.left)
            l = root.left
        if root.right:
            self.invertTree(root.right)
            r = root.right
        
        root.left = r
        root.right = l
        return root

