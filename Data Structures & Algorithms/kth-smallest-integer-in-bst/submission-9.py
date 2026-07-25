# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sizeSubTree(self, root, dico):
        if not root:
            dico[root] = 0
            return 0

        r, l = self.sizeSubTree(root.right, dico), self.sizeSubTree(root.left, dico)
        dico[root] = r + l + 1
        return r + l + 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dico = dict()
        self.sizeSubTree(root, dico)
        
        while True:
            l, r = dico[root.left], dico[root.right]

            if l+1 == k:
                return root.val
            
            if l+1 > k:
                root = root.left
            else:
                root = root.right
                k = k-l-1