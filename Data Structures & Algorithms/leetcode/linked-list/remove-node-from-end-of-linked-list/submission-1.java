/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode ptr1 = null;
        ListNode ptr2 = head;
        int nbSteps = 0;

        while (nbSteps < n-1) {
            ptr2 = ptr2.next;
            nbSteps++;
        }

        while (ptr2.next != null) {
            ptr2 = ptr2.next;
            if (ptr1 == null) {
                ptr1 = head;
            }
            else {
                ptr1 = ptr1.next;
            }
        }

        if (ptr1 == null) {
            return head.next;
        }

        ptr1.next = ptr1.next.next;
        return head;
    }
}
