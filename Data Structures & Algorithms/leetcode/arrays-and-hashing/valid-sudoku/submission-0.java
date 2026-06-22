class Solution {
    public boolean isValidRow(char[] row) {
        HashSet<Character> visited = new HashSet<>();

        for (int i = 0; i < 9; i++) {
            if (row[i] != '.' && !visited.contains(row[i])) {
                visited.add(row[i]);
            }
            else if (row[i] != '.') {
                return false;
            }
        }

        return true;
    }

    public boolean isValidSquare(char[][] square) {
        HashSet<Character> visited = new HashSet<>();

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (square[i][j] != '.' && !visited.contains(square[i][j])) {
                    visited.add(square[i][j]);
                }
                else if (square[i][j] != '.') {
                    return false;
                } 
            }
        }

        return true;
    }

    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            char[] column = new char[9];
            for (int j = 0; j < 9; j++) {
                column[j] = board[j][i];
            }
            if (!isValidRow(board[i]) || !isValidRow(column)) {
                return false;
            }
        }

        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                char[][] square = new char[3][3];
                
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        square[k][l] = board[i+k][j+l];
                    }
                }

                if (!isValidSquare(square)) {
                    return false;
                }
            }
        }

        return true;
    }
}
