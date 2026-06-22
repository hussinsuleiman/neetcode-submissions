class Solution {
    public int dfs(int i, int j, boolean[][] visited, int[][] grid) {
        int IslandSize = 1;
        visited[i][j] = true;
        
        if (0 < i && !visited[i-1][j] && grid[i-1][j] == 1) {
            IslandSize += dfs(i-1, j, visited, grid);
        }
        if (0 < j && !visited[i][j-1] && grid[i][j-1] == 1) {
            IslandSize += dfs(i, j-1, visited, grid);
        }
        if (grid.length-1 > i && !visited[i+1][j] && grid[i+1][j] == 1) {
            IslandSize += dfs(i+1, j, visited, grid);
        }
        if (grid[0].length-1 > j && !visited[i][j+1] && grid[i][j+1] == 1) {
            IslandSize += dfs(i, j+1, visited, grid);
        }

        return IslandSize;
    }

    public int maxAreaOfIsland(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int maxIsland = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    int IslandSize = dfs(i, j, visited, grid);
                    if (IslandSize > maxIsland) {
                        maxIsland = IslandSize;
                    }
                }
            }
        }

        return maxIsland;
    }
}
