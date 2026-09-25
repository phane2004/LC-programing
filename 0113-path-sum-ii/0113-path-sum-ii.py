# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        if root == None:
            return []
        def helper(root, temp, t):
            # print(root)
            # print(temp, " target =", t)
            if  t == 0 and not root.left and not root.right:
                res.append(temp[:])
                return
            if root.left:
                temp.append(root.left.val)
                helper(root.left, temp, t - root.left.val)
                temp.pop()
            if root.right:
                temp.append(root.right.val)
                helper(root.right, temp, t - root.right.val)
                temp.pop()
        r = root
        temp = [root.val]
        t = targetSum - root.val
        # print(r.val)
        helper(r, temp, t)
        return res