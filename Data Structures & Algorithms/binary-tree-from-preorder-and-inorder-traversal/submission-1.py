# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        i = 0
        
        while inorder[i] != preorder[0]:
            i += 1
        
        leftIn = inorder[:i]
        rightIn = inorder[i+1:]
        eltsR = set(rightIn)
        rightPre = []
        leftPre = []

        for k in range(1, len(preorder)):
            if preorder[k] in eltsR:
                rightPre.append(preorder[k])
            else:
                leftPre.append(preorder[k])

        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)

        return root
            

