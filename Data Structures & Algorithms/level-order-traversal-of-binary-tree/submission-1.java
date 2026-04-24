/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();

        if (root == null) {
            return output;
        }

        LinkedList<TreeNode> list = new LinkedList<TreeNode>();
        list.addFirst(root);
        int inLevel = 1;

        while (inLevel > 0) {
            List<Integer> level = new ArrayList<Integer>();

            for (int i = 0; i < inLevel; i++) {
                TreeNode node = list.removeLast();
                if (node.left != null) {
                    list.addFirst(node.left);
                }
                if (node.right != null) {
                    list.addFirst(node.right);
                }
                level.add(node.val);
            }

            output.add(level);
            inLevel = list.size();
        }

        return output;
    }
}
