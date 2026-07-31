class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            elts1 = set()
            elts2 = set()

            for j in range(9):
                if (board[i][j].isdigit() and board[i][j] in elts1) or (board[j][i].isdigit() and board[j][i] in elts2):
                    return False

                elts1.add(board[i][j])
                elts2.add(board[j][i])

        for i in range(0,9,3):
            for j in range(0,9,3):
                elts = set()

                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l].isdigit() and board[i+k][j+l] in elts:
                            return False    
                        elts.add(board[i+k][j+l])
        
        return True