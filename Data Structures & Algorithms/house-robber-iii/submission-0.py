# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node):
            if not node:
                memo[node] = 0
                return
            
            dp(node.left)
            dp(node.right)

            ll = memo[node.left.left] if node.left else 0
            lr = memo[node.left.right] if node.left else 0
            rl = memo[node.right.left] if node.right else 0
            rr = memo[node.right.right] if node.right else 0
            memo[node] = max(memo[node.left] + memo[node.right], node.val + ll + lr + rl + rr)
        
        dp(root)
        return memo[root]