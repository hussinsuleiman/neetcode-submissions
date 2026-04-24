/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        HashMap<Node, Node> oldToNew = new HashMap<>();
        return addNewNode(node, oldToNew);
    }

    public Node addNewNode(Node node, HashMap<Node, Node> oldToNew) {
        if (oldToNew.containsKey(node)) {
            return oldToNew.get(node);
        }

        Node newNode = new Node(node.val);
        oldToNew.put(node, newNode);

        for (int i = 0; i < node.neighbors.size(); i++) {
            newNode.neighbors.add(addNewNode(node.neighbors.get(i), oldToNew));
        }

        return newNode;
    }
}