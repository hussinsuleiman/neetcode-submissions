# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = -float('inf')

        def dfs(node):
            if not node:
                return 0
        
            gain_left = max(0, dfs(node.left))
            gain_right = max(0, dfs(node.right))
            self.answer = max(self.answer, node.val + gain_left + gain_right)
            return node.val + max(gain_left, gain_right)

        dfs(root)
        return self.answer