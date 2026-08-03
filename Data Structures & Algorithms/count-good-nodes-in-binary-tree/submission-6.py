# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, x):
            if node.left:
                dfs(node.left, max(x, node.left.val))

            if node.right:
                dfs(node.right, max(x, node.right.val))

            if node.val >= x:
                res[0] += 1

        dfs(root, root.val)
        return res[0]