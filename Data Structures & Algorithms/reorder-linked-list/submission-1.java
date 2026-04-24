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

    public void reorderList(ListNode head) {
        ListNode ptr1 = head;
        ListNode ptr2 = head;

        while (ptr2 != null && ptr2.next != null) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next.next;
        }

        ListNode newHead = reverseList(ptr1);

        while (head != ptr1 && newHead != ptr1) {
            ListNode temp = head.next;
            head.next = newHead;
            head = temp;
            
            if (newHead.next == head) {
                break;
            }
            
            temp = newHead.next;
            newHead.next = head;
            newHead = temp;
        }
    }
}
