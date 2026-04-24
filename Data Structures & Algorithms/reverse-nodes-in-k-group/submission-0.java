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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return head;
        }

        ListNode next = head.next;
        head.next = null;
        ListNode newHead = reverseList(next);
        next.next = head;

        return newHead;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode ptr = head;

        for (int i = 0; i < k-1; i++) {
            if (ptr.next == null) {
                return head;
            }
            ptr = ptr.next;
        }

        if (ptr.next == null) {
            return reverseList(head);
        }
        ListNode temp = ptr.next;
        ptr.next = null;

        ListNode newHead = reverseList(head);
        head.next = reverseKGroup(temp, k);
        
        return newHead;
    }
}
