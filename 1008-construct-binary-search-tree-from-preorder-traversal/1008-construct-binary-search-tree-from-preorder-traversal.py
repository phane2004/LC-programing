# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, val, root):
        if val < root.val and root.left == None:
            root.left = TreeNode(val)
        elif val > root.val and root.right == None:
            root.right = TreeNode(val)
        if val < root.val:
            self.construct(val, root.left)
        if val > root.val:
            self.construct(val, root.right)
        
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        root = TreeNode(preorder[0])

        for i in range(1, len(preorder)):
            self.construct(preorder[i], root)
        return root
        