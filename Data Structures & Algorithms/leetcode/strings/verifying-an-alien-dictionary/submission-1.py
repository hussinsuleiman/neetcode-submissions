class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ranks = dict()
        ranks[" "] = 0

        for i in range(26):
            ranks[order[i]] = i+1
        
        maxLen = 0
        board = []

        for i in range(len(words)):
            l = len(words[i])

            if l > maxLen:
                maxLen = l

        for word in words:
            line = list(word)

            for k in range(len(line), maxLen):
                line.append(" ")

            board.append(line)
        
        for m in range(1, len(words)):
            for k in range(maxLen):
                if ranks[board[m][k]] > ranks[board[m-1][k]]:
                    break
                    
                if ranks[board[m][k]] < ranks[board[m-1][k]]:
                    return False

        return True