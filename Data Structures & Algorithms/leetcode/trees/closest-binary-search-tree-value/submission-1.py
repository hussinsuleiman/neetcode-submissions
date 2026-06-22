# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return float('inf')
        
        cur = root.val

        if cur <= target:
            r = self.closestValue(root.right, target)

            if abs(r-target) < target-cur:
                return r
            
            return cur
        
        l = self.closestValue(root.left, target)

        if abs(l-target) <= cur-target:
            return l
        
        return cur