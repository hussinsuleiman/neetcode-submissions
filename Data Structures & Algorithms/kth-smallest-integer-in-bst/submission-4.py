# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sizeSubTree(self, root):
        if not root:
            return 0
        return 1 + self.sizeSubTree(root.right) + self.sizeSubTree(root.left)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l, r = self.sizeSubTree(root.left), self.sizeSubTree(root.right)

        if l+1 == k:
            return root.val
        
        if l+1 > k:
            return self.kthSmallest(root.left, k)

        return self.kthSmallest(root.right, k-l-1)