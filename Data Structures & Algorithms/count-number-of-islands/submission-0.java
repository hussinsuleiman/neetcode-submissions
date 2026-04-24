class Solution {
    public void dfs(int i, int j, boolean[][] visited, char[][] grid) {
        visited[i][j] = true;
        
        if (0 < i && !visited[i-1][j] && grid[i-1][j] == '1') {
            dfs(i-1, j, visited, grid);
        }
        if (0 < j && !visited[i][j-1] && grid[i][j-1] == '1') {
            dfs(i, j-1, visited, grid);
        }
        if (grid.length-1 > i && !visited[i+1][j] && grid[i+1][j] == '1') {
            dfs(i+1, j, visited, grid);
        }
        if (grid[0].length-1 > j && !visited[i][j+1] && grid[i][j+1] == '1') {
            dfs(i, j+1, visited, grid);
        }
    }

    public int numIslands(char[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int nbIslands = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    nbIslands += 1;
                    dfs(i, j, visited, grid);
                }
            }
        }

        return nbIslands;
    }
}
