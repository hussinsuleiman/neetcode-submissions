class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int nbFresh = 0;
        int time = 0;
        int m = grid.length;
        int n = grid[0].length; 

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.add(new int[] {i, j});
                }
                else if (grid[i][j] == 1) {
                    nbFresh++;
                } 
            }
        }

        int[][] dirs = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

        while (nbFresh > 0 && q.size() > 0) {
            int s = q.size();

            for (int k = 0; k < s; k++) {
                int[] rotten = q.poll();
                int row = rotten[0];
                int col = rotten[1];

                for (int i = 0; i < 4; i++) {    
                    int r = row + dirs[i][0];
                    int c = col + dirs[i][1];
                    
                    if (r >= 0 && c >= 0 && r < m && c < n && grid[r][c] == 1) {
                        grid[r][c] = 2;
                        q.add(new int[] {r, c});
                        nbFresh--;
                    }
                }
            }
            
            time++;
        }
        
        if (nbFresh == 0) {
            return time;
        }
        return -1;

    }
}
