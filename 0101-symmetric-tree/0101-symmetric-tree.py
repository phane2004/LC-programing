# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bal(p, q):
            
            if not p and not q:
                return True
            if not p or not q:
                return False
            #print(p.val, q.val)
            return p.val == q.val and bal(p.left, q.right) and bal(p.right, q.left)
        return bal(root.left, root.right)