# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not (self.isValidBST(root.left) and self.isValidBST(root.right)):
            return False

        maxLeft = -1000
        minRight = 1000

        if root.left:
            node = root.left

            while node.right:
                node = node.right
            
            maxLeft = node.val
        
        if root.right:
            node = root.right

            while node.left:
                node = node.left
            
            minRight = node.val

        return maxLeft < root.val and root.val < minRight