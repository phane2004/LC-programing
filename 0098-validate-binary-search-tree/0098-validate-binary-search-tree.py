# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    p = float('-inf')
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root == None: return True
        if not self.isValidBST(root.left): return False
        if root.val <= self.p: return False
        self.p = root.val
        return self.isValidBST(root.right)
        