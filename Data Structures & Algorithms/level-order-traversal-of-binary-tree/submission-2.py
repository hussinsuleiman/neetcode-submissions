# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        output = []

        while len(queue) > 0:
            newLevel = []

            for i in range(len(queue)):
                cur = queue.pop(0)
                newLevel.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            output.append(newLevel)
        
        return output
                        


         
