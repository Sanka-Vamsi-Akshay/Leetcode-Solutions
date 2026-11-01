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
        if node is None:
            return None
        map = {1 : Node(1)}
        v = set()
        queue = [node]
        while queue:
            node = queue.pop()
            if node in v:
                continue
            v.add(node)
            if node.val not in map:
                map[node.val] = Node(node.val)
            newNode = map[node.val]
            for n in node.neighbors:
                if n.val not in map:
                    map[n.val] = Node(n.val)
                newNode.neighbors.append(map[n.val])
                queue.append(n)
        return map[1]