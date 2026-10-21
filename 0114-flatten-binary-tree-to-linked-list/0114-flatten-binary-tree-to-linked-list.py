# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        li = []
        def preorder(root):
            if not root:
                return
            li.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        #print(li)
        i = 0
        curr = root
        while i < len(li):
            if i != 0:
                curr.right = TreeNode(li[i])
                curr.left = None
                curr = curr.right
            i += 1
        return root