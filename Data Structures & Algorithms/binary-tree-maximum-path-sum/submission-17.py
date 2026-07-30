# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathWithRootOneSide(r):
            if not r:
                return 0
            
            left, right = max(0, maxPathWithRootOneSide(r.left)), max(0, maxPathWithRootOneSide(r.right))
            return r.val + max(left, right)

        def maxPathWithRootTwoSide(r):
            if not r:
                return 0
            
            left, right = max(0, maxPathWithRootOneSide(r.left)), max(0, maxPathWithRootOneSide(r.right))
            return r.val + left + right

        if not root.left:
            if not root.right:
                return root.val
            return max(maxPathWithRootTwoSide(root), self.maxPathSum(root.right))
        
        if not root.right:
            return max(maxPathWithRootTwoSide(root), self.maxPathSum(root.left))

        return max(maxPathWithRootTwoSide(root), self.maxPathSum(root.left), self.maxPathSum(root.right))