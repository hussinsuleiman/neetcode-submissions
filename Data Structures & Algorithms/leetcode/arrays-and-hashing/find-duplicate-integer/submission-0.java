class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> nbs = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (nbs.contains(nums[i])) {
                return nums[i];
            }
            nbs.add(nums[i]);
        }

        return 0;
    }
}
