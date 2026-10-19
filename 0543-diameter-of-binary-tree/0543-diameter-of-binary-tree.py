# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0
        def dia(root):
            nonlocal m
            if not root:
                return 0
            left = dia(root.left)
            right = dia(root.right)
            m = max(m, (left + right))
            return max(left, right) + 1
        dia(root)
        return m
