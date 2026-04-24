/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        Node newHead = new Node(head.val);
        Node cur = newHead;
        Node node = head;
        HashMap<Node, Node> oldToNew = new HashMap<>();
        oldToNew.put(head, newHead);

        while (node.next != null) {
            node = node.next;
            Node next = new Node(node.val);
            cur.next = next;
            cur = next;
            oldToNew.put(node, cur);
        }

        for (Node n : oldToNew.keySet()) {
            oldToNew.get(n).random = oldToNew.get(n.random);
        }

        return newHead;
    }
}
