# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tmp = res
        head = head.next
        while head:
            tot = 0
            while head and head.val != 0:
                tot += head.val
                head = head.next
            tmp.next = ListNode(tot)
            tmp = tmp.next
            head = head.next
        return res.next