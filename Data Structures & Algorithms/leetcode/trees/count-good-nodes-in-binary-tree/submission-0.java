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
    public List<TreeNode> helper(TreeNode root) {
        List<TreeNode> output = new ArrayList<>();

        if (root == null) {
            return output; 
        }
        
        output.add(root);
        List<TreeNode> left = helper(root.left);
        List<TreeNode> right = helper(root.right);

        for (TreeNode t : left) {
            if (t.val >= root.val) {
                output.add(t);
            }
        }
        for (TreeNode t : right) {
            if (t.val >= root.val) {
                output.add(t);
            }
        }
        
        return output;
    }

    public int goodNodes(TreeNode root) {
        return helper(root).size();
    }
}
