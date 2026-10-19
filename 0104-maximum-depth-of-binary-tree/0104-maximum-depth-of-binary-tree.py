# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(depth, root):
            if not root:
                return depth
            ld = helper(depth + 1, root.left)
            rd = helper(depth + 1, root.right)
            
            #print(ld, rd)
            return max(ld, rd)
        return helper(0, root)