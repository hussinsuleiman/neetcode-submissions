class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None

            board[r][c] = '#'

            for dr, dc in {(-1,0), (1,0), (0,1), (0,-1)}:
                nr, nc = r+dr, c+dc
                if 0 <= nr and nr < rows and 0 <= nc and nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result