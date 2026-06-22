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
        int a = 0;
        int b = 0;
        int pow1 = 1;
        int pow2 = 1;

        ListNode node1 = l1;
        ListNode node2 = l2;

        while (node1 != null) {
            a += pow1 * node1.val;
            node1 = node1.next;
            pow1 *= 10;
        }

        while (node2 != null) {
            b += pow2 * node2.val;
            node2 = node2.next;
            pow2 *= 10;
        }

        int sum = a+b;

        ListNode headNew = new ListNode(sum%10);
        sum = sum/10;
        ListNode nodeNew = headNew;

        while (sum > 0) {
            ListNode nodeNext = new ListNode(sum%10);
            sum = sum/10;
            nodeNew.next = nodeNext;
            nodeNew = nodeNext; 
        }

        return headNew;
    }
}
