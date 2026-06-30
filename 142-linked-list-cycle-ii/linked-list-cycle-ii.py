# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        v = set()
        tmp = head
        while tmp:
            if tmp in v:
                return tmp
            v.add(tmp)
            tmp = tmp.next