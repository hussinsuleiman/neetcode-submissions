# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return []
            
            left, right = dfs(root.left), dfs(root.right)          
            output = [root]

            for node in left:
                if node.val >= root.val:
                    output.append(node)
            
            for node in right:
                if node.val >= root.val:
                    output.append(node)

            return output
        
        return len(dfs(root))

        