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
        HashMap<Node, Integer> nodeToIndex = new HashMap<>();
        HashMap<Integer, Node> indexToNode = new HashMap<>();
        indexToNode.put(0, newHead);
        nodeToIndex.put(head, 0);
        int index = 1;

        while (node.next != null) {
            node = node.next;
            Node next = new Node(node.val);
            cur.next = next;
            cur = next;
            indexToNode.put(index, next);
            nodeToIndex.put(node, index);
            index++;
        }

        for (int i = 0; i < indexToNode.size(); i++) {
            indexToNode.get(i).random = indexToNode.get(nodeToIndex.get(head.random));
            head = head.next;
        }

        return newHead;
    }
}
