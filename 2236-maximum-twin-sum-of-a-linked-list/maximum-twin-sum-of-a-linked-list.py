# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s = f = head
        pre = None
        while f.next.next:
            s.prev = pre
            pre = s
            s = s.next
            f = f.next.next
        s.prev = pre
        res = 0
        f = s.next
        while s:
            v = s.val + f.val
            if v > res:
                res = v
            s = s.prev
            f = f.next
        return res