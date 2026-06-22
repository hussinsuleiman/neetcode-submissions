class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> nbs = new HashSet<>();
        HashSet<Integer> possibleStarts = new HashSet<>();
        int maxLen = 0;

        for (int i = 0; i < nums.length; i++) {
            nbs.add(nums[i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (!nbs.contains(nums[i]-1)) {
                possibleStarts.add(nums[i]);
            }
        }

        for (Integer n : possibleStarts) {
            int len = 1;
            int k = n;

            while (nbs.contains(k+1)) {
                len++;
                k++;
            }

            if (len > maxLen) {
                maxLen = len;
            }
        }

        return maxLen;
    }
}
