# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def search(root):
            if not root:
                return
            #print(root.val)
            if val == root.val:
                return root
            if val < root.val:
                node = search(root.left)
                return node
            else:
                node = search(root.right)
                return node
            return None
        return search(root)
             