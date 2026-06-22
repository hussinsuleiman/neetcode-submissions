# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def preorder(self, root, depth):
        if not root:
            return []
        
        left = self.preorder(root.left, depth + 1)
        right = self.preorder(root.right, depth + 1)
        dash = ['-'] * depth
        return dash + [str(root.val)] + left + ['/'] + right
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        s = self.preorder(root, 0)
        serial = ''.join(s)
        return serial
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        n = len(data)
        i = 0
        stack = []
        right = False

        while i < n:
            if data[i] == '/':
                right = True
                i += 1
                continue

            depth = 0

            while i < n and data[i] == '-':
                depth += 1
                i += 1
            
            value = 0

            while i < n and data[i].isdigit():
                value = 10 * value + int(data[i])
                i += 1
            
            node = TreeNode(value)

            while len(stack) > depth:
                stack.pop()
            
            if stack:
                parent = stack[-1]

                if parent.left or right:
                    parent.right = node
                    right = False
                else:
                    parent.left = node
                
            stack.append(node)
        
        return stack[0]