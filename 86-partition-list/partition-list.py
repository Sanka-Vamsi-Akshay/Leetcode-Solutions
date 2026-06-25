# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = ListNode()
        h2 = ListNode()
        tmp1 = h1
        tmp2 = h2
        tmp = head
        while tmp:
            if tmp.val < x:
                tmp1.next = tmp
                tmp1 = tmp1.next
            else:
                tmp2.next = tmp
                tmp2 = tmp2.next
            tmp = tmp.next
        tmp2.next = None
        tmp1.next = h2.next
        return h1.next