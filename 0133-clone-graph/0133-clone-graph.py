"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        root = {node.val: Node(node.val, [])}
        q = deque([node])

        while q:
            n = q.popleft()
            curr = root[n.val]
            for nei in n.neighbors:
                if nei.val not in root:
                    root[nei.val] = Node(nei.val, [])
                    q.append(nei)
                curr.neighbors.append(root[nei.val])
        return root[node.val]