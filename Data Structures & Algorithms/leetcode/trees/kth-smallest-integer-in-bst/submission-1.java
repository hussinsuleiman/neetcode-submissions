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
    int rank = 1;

    public int kthSmallest(TreeNode root, int k) {
        if (root.left == null) {
            if (rank == k) {
                return root.val;
            }
            if (root.right == null) {
                return -1;
            }
            rank++;
            return kthSmallest(root.right, k);        
        }

        int left = kthSmallest(root.left, k);
        if (left != -1) {
            return left;
        }
        
        rank++;
        if (rank == k) {
            return root.val;
        }
        if (root.right == null) {
            return -1;
        }

        rank++;
        int right = kthSmallest(root.right, k);
        
        if (right != -1) {
            return right;
        } 
        
        return -1;
    }
}
