# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        li = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            li.append(root.val)
            helper(root.right)
        helper(root)
        print(li)
        return li[k - 1]
    
        