class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBlock(i,j):
            blockNbs = set()
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] != '.' and board[i+k][j+l] in blockNbs:
                        return False
                    blockNbs.add(board[i+k][j+l])
            return True
        
        for i in range(9):
            rowNbs = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in rowNbs:
                    return False
                rowNbs.add(board[i][j])
        
        for i in range(9):
            colNbs = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in colNbs:
                    return False
                colNbs.add(board[j][i])
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkBlock(i,j):
                    return False
        
        return True