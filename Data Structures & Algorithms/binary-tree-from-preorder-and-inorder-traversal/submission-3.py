# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        if n == 0:
            return None

        rootVal = preorder[0]
        root = TreeNode(rootVal)
            
        for i in range(n):
            if inorder[i] == root.val:
                if i == 0:
                    root.right = self.buildTree(preorder[1:], inorder[1:])
                elif i == n-1:
                    root.left = self.buildTree(preorder[1:], inorder[:-1])
                else:
                    root.left = self.buildTree(preorder[1:i+1], inorder[:i])
                    root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
                return root