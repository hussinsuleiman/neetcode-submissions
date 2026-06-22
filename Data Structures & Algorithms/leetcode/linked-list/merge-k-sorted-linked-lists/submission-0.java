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

        ListNode newHead = list2;

        if (list1.val < list2.val) {
            newHead = list1;
            list1 = list1.next;
        }
        else {
            list2 = list2.next;
        }

        newHead.next = mergeTwoLists(list1, list2);
        return newHead;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        int i = 0;
        int j = 0;
        int nbLists = lists.length;

        while (nbLists > 1) {
            j = 0;
            i = 0;

            while (i < nbLists-1) {
                lists[j] = mergeTwoLists(lists[i], lists[i+1]);
                i += 2;
                j++;
            }

            if (i == nbLists-1) {
                lists[j] = lists[i];
                nbLists = j+1;
            }
            else {
                nbLists = j;
            }
        }

        if (nbLists == 0) {
            return null;
        }
        return lists[0];
    }
}
