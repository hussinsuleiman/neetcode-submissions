class Solution {
    public static boolean backtrack(char[][] board, boolean[][] visited, String word, int i, int j, int charIndex) {
        if (charIndex == word.length()) {
            return true;
        }
        visited[i][j] = true;

        if (i < board.length-1) {
            if (board[i+1][j] == word.charAt(charIndex) && !visited[i+1][j]) {
                if (backtrack(board, visited, word, i+1, j, charIndex+1)) {
                    return true;
                }
            }
        }

        if (i > 0) {
            if (board[i-1][j] == word.charAt(charIndex) && !visited[i-1][j]) {
                if (backtrack(board, visited, word, i-1, j, charIndex+1)) {
                    return true;
                }
            }
        }

        if (j < board[i].length-1) {
            if (board[i][j+1] == word.charAt(charIndex) && !visited[i][j+1]) {
                if (backtrack(board, visited, word, i, j+1, charIndex+1)) {
                    return true;
                }
            }
        }

        if (j > 0) {
            if (board[i][j-1] == word.charAt(charIndex) && !visited[i][j-1]) {
                if (backtrack(board, visited, word, i, j-1, charIndex+1)) {
                    return true;
                }
            }
        }

        visited[i][j] = false;
        return false;
    }

    public static boolean exist(char[][] board, String word) {
        ArrayList<Integer> firstLetterXCoord = new ArrayList<>();
        ArrayList<Integer> firstLetterYCoord = new ArrayList<>();
        char firstLetter = word.charAt(0);

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == firstLetter) {
                    firstLetterXCoord.add(i);
                    firstLetterYCoord.add(j);
                }
            }
        }

        for (int i = 0; i < firstLetterXCoord.size(); i++) {
            boolean[][] visited = new boolean[board.length][board[0].length];
            if (backtrack(board, visited, word, firstLetterXCoord.get(i), firstLetterYCoord.get(i), 1)) {
                return true;
            }
        }

        return false;
    }
}
