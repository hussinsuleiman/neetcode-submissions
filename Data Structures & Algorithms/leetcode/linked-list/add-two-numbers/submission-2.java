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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode newHead = new ListNode(0);
        ListNode node = newHead;
        ListNode newNode;

        while (l1 != null && l2 != null) {
            node.val += l1.val + l2.val;
            newNode = new ListNode(0);

            if (node.val >= 10) {
                node.val %= 10;
                newNode.val = 1;
            }

            l1 = l1.next;
            l2 = l2.next;
            if (l1 == null && l2 == null && newNode.val == 0) {
                break;
            }
            node.next = newNode;
            node = newNode;
        }

        while (l2 != null) {
            node.val += l2.val;
            newNode = new ListNode(0);

            if (node.val >= 10) {
                node.val %= 10;
                newNode.val = 1;
            }

            l2 = l2.next;
            if (l2 == null && newNode.val == 0) {
                break;
            }
            node.next = newNode;
            node = newNode;
        }

        while (l1 != null) {
            node.val += l1.val;
            newNode = new ListNode(0);

            if (node.val >= 10) {
                node.val %= 10;
                newNode.val = 1;
            }

            l1 = l1.next;
            if (l1 == null && newNode.val == 0) {
                break;
            }
            node.next = newNode;
            node = newNode;
        }

        return newHead;
    }
}
