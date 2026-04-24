class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int m = grid.length;
        int n = grid[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    q.add(new int[] {i, j});
                }
            }
        }

        int[][] dirs = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

        while (q.size() > 0) {
            int[] cur = q.poll();
            int row = cur[0];
            int col = cur[1];

            for (int i = 0; i < 4; i++) {
                int r = row + dirs[i][0];
                int c = col + dirs[i][1];

                if (r >= 0 && r < m && c >=0 && c < n && grid[r][c] == Integer.MAX_VALUE) {
                    grid[r][c] = grid[row][col] + 1;
                    q.add(new int[] {r, c}); 
                }
            } 
        }
    }
}
