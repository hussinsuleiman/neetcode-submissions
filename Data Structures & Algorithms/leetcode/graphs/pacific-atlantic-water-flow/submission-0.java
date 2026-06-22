class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        boolean[][] canReachPacific = new boolean[m][n];
        boolean[][] canReachAtlantic = new boolean[m][n];
        List<List<Integer>> output = new ArrayList<List<Integer>>(); 

        for (int i = 0; i < m; i++) {
            dfs(i, 0, canReachPacific, heights[i][0], heights, m, n);
            dfs(i, n-1, canReachAtlantic, heights[i][n-1], heights, m, n);
        }

        for (int j = 0; j < n; j++) {
            dfs(0, j, canReachPacific, heights[0][j], heights, m, n);
            dfs(m-1, j, canReachAtlantic, heights[m-1][j], heights, m, n);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (canReachPacific[i][j] && canReachAtlantic[i][j]) {
                    List<Integer> element = new ArrayList<Integer>();
                    element.add(i);
                    element.add(j);
                    output.add(element);
                }
            }
        }

        return output;
    }

    public void dfs(int i, int j, boolean[][] visit, int minVal, int[][] heights, int m, int n) {
        if (i >= 0 && i < m && j >= 0 && j < n && heights[i][j] >= minVal && !visit[i][j]) {
            visit[i][j] = true;
            dfs(i-1, j, visit, heights[i][j], heights, m, n);
            dfs(i+1, j, visit, heights[i][j], heights, m, n);
            dfs(i, j-1, visit, heights[i][j], heights, m, n);
            dfs(i, j+1, visit, heights[i][j], heights, m, n);
        } 
    }
}
