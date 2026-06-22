class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> nbsToIndices = new HashMap<>();
        int[] output = new int[2];

        for (int i = 0; i < nums.length; i++) {
            if (nbsToIndices.containsKey(nums[i])) {
                output[0] = nbsToIndices.get(nums[i]);
                output[1] = i;
                break;
            }
            nbsToIndices.put(target-nums[i], i);
        }

        return output;
    }
}
