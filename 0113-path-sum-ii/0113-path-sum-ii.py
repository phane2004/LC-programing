# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        temp = []
        def dfs(root, currSum):
            if not root:
                return
            temp.append(root.val)
            currSum += root.val
            if not root.left and not root.right:
                if currSum == targetSum:
                    res.append(temp[:])
                temp.pop()
                return
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            temp.pop()
        dfs(root, 0)
        return res
