class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        L = len(word)
        m,n = len(board), len(board[0])
        seen = set()

        def backtrack(i, a, b, seen):
            if i == L:
                return True

            if a < 0 or a >= m or b < 0 or b >= n or word[i] != board[a][b] or (a,b) in seen:
                return False
            
            seen.add((a,b))
            nxt = {(a+1, b), (a, b+1), (a-1, b), (a, b-1)}
            found = False

            for (x,y) in nxt:
                found = found or backtrack(i+1, x, y, seen)
            
            seen.remove((a,b))
            return found
        
        for a in range(m):
            for b in range(n):
                if backtrack(0, a, b, seen):
                    return True

        return False