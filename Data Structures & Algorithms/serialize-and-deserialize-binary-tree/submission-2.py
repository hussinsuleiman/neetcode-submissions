# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        values = []

        def dfs(node):
            if not node:
                values.append('n')
                return

            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(values)

    def deserialize(self, data):
        values = data.split(',')
        i = 0

        def dfs():
            nonlocal i

            token = values[i]
            i += 1

            if token == 'n':
                return None

            node = TreeNode(int(token))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()