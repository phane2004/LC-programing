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
        q = []
        q.append(root)
        depth = 0
        while len(q) > 0:
            depth += 1
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                print(node.val, end = " ")
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            print()
            print(depth)
        return depth
