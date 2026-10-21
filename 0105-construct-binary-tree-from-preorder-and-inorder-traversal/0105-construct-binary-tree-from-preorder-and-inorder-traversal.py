# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def build(inorder):
            if inorder:
                idx = inorder.index(preorder.pop(0))
                root = TreeNode(inorder[idx])
                root.left = build(inorder[:idx])
                root.right = build(inorder[idx + 1: ])
                return root
        return build(inorder)
