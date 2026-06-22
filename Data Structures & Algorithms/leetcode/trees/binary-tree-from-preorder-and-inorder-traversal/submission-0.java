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
    int indexPreorder = 1;
    HashMap<Integer, Integer> inOrderIndices = new HashMap<>();

    public TreeNode dfs(int[] preorder, int[] inorder, int l, int r) {
        if (l > r) {
            return null;
        }
        
        TreeNode root = new TreeNode(preorder[indexPreorder]);
        int indexInOrder = inOrderIndices.get(preorder[indexPreorder++]);

        root.left = dfs(preorder, inorder, l, indexInOrder-1);
        root.right = dfs(preorder, inorder, indexInOrder+1, r);
        return root;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        TreeNode root = new TreeNode(preorder[0]);
        
        for (int i = 0; i < inorder.length; i++) {
            inOrderIndices.put(inorder[i], i);
        }

        root.left = dfs(preorder, inorder, 0, inOrderIndices.get(preorder[0])-1);
        root.right = dfs(preorder, inorder, inOrderIndices.get(preorder[0])+1, inorder.length-1);
        return root;
    }
}
