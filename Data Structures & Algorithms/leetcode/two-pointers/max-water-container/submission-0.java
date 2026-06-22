class Solution {
    public int maxArea(int[] heights) {
        int i = 0;
        int j = heights.length-1;
        int maxVolume = 0;

        while (j > i) {
            int a = Math.min(heights[i], heights[j]);
            int volume = (j-i) * a;
            if (volume > maxVolume) {
                maxVolume = volume;
            }

            if (a == heights[i]) {
                i++;
            }
            else {
                j--;
            }
        }

        return maxVolume;
    }
}
