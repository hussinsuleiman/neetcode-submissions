class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        n = len(word)

        for i in range(n):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()

            node = node.children[word[i]]
        
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            
            node = node.children[word[i]]
        
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                return False
            
            node = node.children[prefix[i]]
        
        return True      