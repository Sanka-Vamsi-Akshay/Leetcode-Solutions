# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        v = set()
        tmp = headA
        while tmp:
            v.add(tmp)
            tmp = tmp.next
        tmp = headB
        while tmp and tmp not in v:
            tmp = tmp.next
        return tmp