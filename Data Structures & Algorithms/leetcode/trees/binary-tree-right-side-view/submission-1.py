# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        output = [root.val] 
        rBranch = self.rightSideView(root.right)
        lBranch = self.rightSideView(root.left)
        output += rBranch

        for i in range(len(rBranch), len(lBranch)):
            output.append(lBranch[i])
        
        return output
        
         