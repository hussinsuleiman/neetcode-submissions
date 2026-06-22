class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] nbWays = new int[n];
        nbWays[0] = 1;
        nbWays[1] = 2;
        for (int i = 2; i < n; i++) {
            nbWays[i] = nbWays[i-1] + nbWays[i-2];
        }
        return nbWays[n-1];
    }
}
