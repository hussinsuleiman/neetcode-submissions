# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, x):
            if not root:
                return []
            
            left, right = [], []

            if root.left:   
                left = dfs(root.left, root.left.val)
            if root.right:
                right = dfs(root.right, root.right.val)
            
            output = [root]

            for node in left:
                if node.val >= x:
                    output.append(node)
            
            for node in right:
                if node.val >= x:
                    output.append(node)

            return output
        
        return len(dfs(root, root.val))

        