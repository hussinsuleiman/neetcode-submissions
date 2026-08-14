# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            if not root.left:
                return root.right
            
            node = root.left

            while node.right:
                node = node.right

            node.right = root.right
            return root.left

        par = root
        node = root.left
        sideLeft = True 

        if root.val < key:
            node = root.right
            sideLeft = False

        while node and node.val != key:
            par = node

            if node.val > key:
                node = node.left
                sideLeft = True 
            else:
                node = node.right
                sideLeft = False

        if not node:
            return root
        
        if sideLeft:
            if not node.left:
                par.left = node.right
            else:
                par.left = node.left
                cur = node.left

                while cur.right:
                    cur = cur.right
                
                cur.right = node.right

        else:
            if not node.left:
                par.right = node.right
            else:
                par.right = node.left
                cur = node.left

                while cur.right:
                    cur = cur.right
                
                cur.right = node.right

        return root