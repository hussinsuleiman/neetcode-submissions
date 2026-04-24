class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        
        for i in range(n):
            col = []

            for j in range(n):
                if len(words[j]) > i:
                    col.append(words[j][i])

            if ''.join(col) != words[i]:
                return False

        return True