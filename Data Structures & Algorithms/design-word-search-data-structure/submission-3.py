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

        def searchNode(index, node):
            if index == l:
                return node.is_word

            char = word[index]

            if char == '.':
                for child in node.children.values():
                    if searchNode(index+1, child):
                        return True
                return False

            if char not in node.children:
                return False

            node = node.children[char]
            return searchNode(index+1, node)

        return searchNode(0, r)