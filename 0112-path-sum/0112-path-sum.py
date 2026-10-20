# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        q = [[root, root.val]]
        while q:
            for _ in range(len(q)):
                root, val = q.pop(0)
                #print(val)
                if not root.left and not root.right and val == targetSum:
                    return True
                if root.left:
                    q.append([root.left, val + root.left.val])
                if root.right:
                    q.append([root.right, val + root.right.val])
        return False
            
