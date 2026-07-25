# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        dico = dict()

        if n == 0:
            return None
        
        for i in range(n):
            dico[inorder[i]] = i

        rootVal = preorder[0]
        root = TreeNode(rootVal)
        ind = dico[rootVal]
            
        if ind == 0:
            root.right = self.buildTree(preorder[1:], inorder[1:])
        elif ind == n-1:
            root.left = self.buildTree(preorder[1:], inorder[:-1])
        else:
            root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
            root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        return root