# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        tmp = []
        res = []
        idx = 0
        while head:
            res.append(0)
            while tmp and tmp[-1][0] < head.val:
                v = tmp.pop()
                res[v[1]] = head.val
            tmp.append((head.val, idx))
            head = head.next
            idx += 1
        return res