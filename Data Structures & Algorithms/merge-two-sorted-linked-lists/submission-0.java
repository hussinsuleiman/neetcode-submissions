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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        ListNode head = list1;
        if (list2.val < list1.val) {
            head = list2;
        }
        ListNode prev = new ListNode();

        if (head == list1) {
            prev = mergeTwoLists(list1.next, list2);
        }
        else {
            prev = mergeTwoLists(list1, list2.next);
        }

        head.next = prev;
        return head;
    }
}