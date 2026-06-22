class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] minSub = new int[n+1];
        
        for (int i = 2; i <= n; i++) {
            minSub[i] = Math.min(minSub[i-1] + cost[i-1], minSub[i-2] + cost[i-2]);
        }

        return minSub[n];
    }
}
