# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root
        def helper(root):
            if not root:
                return
            left = root.left
            right = root.right
            root.left, root.right = right, left
            helper(root.left)
            helper(root.right)
        helper(root)
        return root