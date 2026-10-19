# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def bal(root):
            if not root:
                return 0
            left = bal(root.left)
            if left == -1:
                return -1
            right = bal(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            # print(left, right, end= " ")
            # print()
            return max(left, right) + 1
        return bal(root) != -1
            