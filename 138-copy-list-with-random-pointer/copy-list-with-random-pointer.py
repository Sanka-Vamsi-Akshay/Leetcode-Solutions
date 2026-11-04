"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        map = {None : None}
        tmp = head
        while tmp:
            map[tmp] = Node(tmp.val)
            tmp = tmp.next
        tmp = head
        while tmp:
            map[tmp].next = map[tmp.next]
            map[tmp].random = map[tmp.random]
            tmp = tmp.next
        return map[head]