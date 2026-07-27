class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        
        node.is_word = True

    def search(self, word: str) -> bool:
        r = self.root
        l = len(word)

        def searchNode(w, node, n):
            for i in range(n):
                char = w[i]

                if char == '.':
                    for child in node.children:
                        if searchNode(w[i+1:], node.children[child], n-1-i):
                            return True
                    return False

                if char not in node.children:
                    return False

                node = node.children[char]

            return node.is_word

        return searchNode(word, r, l)