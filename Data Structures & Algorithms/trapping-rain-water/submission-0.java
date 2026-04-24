class Solution {
    public int trap(int[] height) {
        int[] prefix = new int[height.length];
        int[] suffix = new int[height.length];
        prefix[0] = 0;
        suffix[height.length-1] = 0;
        int maxPrefix = 0;
        int maxSuffix = 0;

        for (int i = 0; i < height.length-1; i++) {
            if (height[i] > maxPrefix) {
                maxPrefix = height[i];
            }
            prefix[i+1] = maxPrefix;
        }

        for (int i = height.length-1; i > 0; i--) {
            if (height[i] > maxSuffix) {
                maxSuffix = height[i];
            }
            suffix[i-1] = maxSuffix;
        }

        int totalArea = 0;

        for (int i = 0; i < height.length; i++) {
            int localArea = Math.min(prefix[i], suffix[i]) - height[i];
            if (localArea > 0) {
                totalArea += localArea;
            }
            
        }

        return totalArea;
    }
}
