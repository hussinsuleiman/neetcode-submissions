# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minBST(self, root):
        if not root:
            return 1001
        while root.left:
            root = root.left
        return root.val
    
    def maxBST(self, root):
        if not root:
            return -1001
        while root.right:
            root = root.right
        return root.val

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not (self.isValidBST(root.right) and self.isValidBST(root.left)):
            return False
        
        m, M = self.maxBST(root.left), self.minBST(root.right)
        return (m < root.val and root.val < M)