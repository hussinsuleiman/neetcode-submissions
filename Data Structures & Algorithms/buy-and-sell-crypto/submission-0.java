class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 1) {
            return 0;
        }

        int i = 0;
        int j = 0;
        int profit = 0;

        while (j < prices.length) {
            while (j+1 < prices.length && prices[j+1] >= prices[j]) {
                j++;
            }
            profit = Math.max(profit, prices[j] - prices[i]);
            j++;
            if (j < prices.length && prices[j] < prices[i]) {
                i = j;
            }
        }

        return profit;
    }
}
