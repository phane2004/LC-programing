# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root == p or root == q:
            return root
        # elif root.val < p.val and root.val < q.val:
        #     root = root.right
        # elif root.val > p.val and root.val > q.val:
        #     root = root.left
        #if root.val > p.val or root.val > q.val:
        left = self.lowestCommonAncestor(root.left, p, q)
        #if root.val < p.val or root.val < p.val:
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left:
            return right
        return left