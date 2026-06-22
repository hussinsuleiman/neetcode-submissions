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
    public int findMaxInBST(TreeNode root) {
        while (root.right != null) {
            root = root.right;
        }

        return root.val;
    }

    public int findMinInBST(TreeNode root) {
        while (root.left != null) {
            root = root.left;
        }

        return root.val;
    }

    public boolean isValidBST(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) {
            return true;
        }
        if (root.left == null) {
            return isValidBST(root.right) && root.val < findMinInBST(root.right);
        }
        if (root.right == null) {
            return isValidBST(root.left) && root.val > findMaxInBST(root.left);
        }
        return isValidBST(root.left) && isValidBST(root.right) && root.val > findMaxInBST(root.left) && root.val < findMinInBST(root.right);
    }
}
