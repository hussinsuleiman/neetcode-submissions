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
    public void reorderList(ListNode head) {
        ArrayList<ListNode> nodes = new ArrayList<>();
        ListNode node = head;
        
        while (node != null) {
            nodes.add(node);
            node = node.next;
        }
        
        int n = nodes.size();
        int i = 0; 
        int j = n-1;
        
        while (i <= j) {
            if (i < j) {
                nodes.get(i).next = nodes.get(j);
                i++;
            }
            else {
                nodes.get(i).next = null;
                break;
            }
            if (i < j) {
                nodes.get(j).next = nodes.get(i);
                j--;
            }
            else {
                nodes.get(j).next = null;
            }
        }
    }
}
