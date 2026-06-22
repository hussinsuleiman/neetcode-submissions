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
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(maxDepth(root.right), maxDepth(root.left))+1;
    }

    public int diameterOfBinaryTree(TreeNode root) {
        if (root.right == null && root.left == null) {
            return 0;
        }
        
        int a = maxDepth(root.right) + maxDepth(root.left);
        int b = 0;
        int c = 0;

        if (root.right != null) {
            b = maxDepth(root.right.left) + maxDepth(root.right.right);
        }
        if (root.left != null) {
            c = maxDepth(root.left.left) + maxDepth(root.left.right);
        }

        return Math.max(Math.max(a,b),c);
    }
}
