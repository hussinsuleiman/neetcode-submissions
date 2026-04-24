class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> nbs = new HashMap<>();
        int[] output = new int[2];

        for (int i = 0; i < nums.length; i++) {
            if (!nbs.containsKey(nums[i])) {
                nbs.put(nums[i], i);
            }
            else if (target%2 == 0 && nums[i] == target/2) {
                output[0] = nbs.get(nums[i]);
                output[1] = i;
                return output;
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nbs.keySet().contains(target-nums[i]) && 2*nums[i] != target) {
                output[0] = nbs.get(nums[i]);
                output[1] = nbs.get(target-nums[i]);
                return output;
            }
        } 

        return output;
    }
}
