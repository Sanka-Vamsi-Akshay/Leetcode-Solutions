import java.util.Set;
import java.util.HashSet;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> v = new HashSet<ListNode>();
        ListNode tmp = headB;
        while(tmp != null){
            v.add(tmp);
            tmp = tmp.next;
        }
        tmp = headA;
        while(tmp != null && !v.contains(tmp)){
            tmp = tmp.next;
        }
        return (tmp != null) ? tmp : null;
    }
}