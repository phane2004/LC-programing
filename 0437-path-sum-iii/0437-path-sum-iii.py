# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        if not root:return 0
        q = [root]
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                def dfs(node, currSum):
                    nonlocal count
                    if not node:
                        return
                    currSum += node.val
                    if currSum == targetSum:
                        count += 1
                    dfs(node.left, currSum)
                    dfs(node.right, currSum)
                dfs(node, 0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return count