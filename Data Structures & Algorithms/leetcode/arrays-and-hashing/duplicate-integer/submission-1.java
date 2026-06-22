class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> nbs = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (nbs.contains(nums[i])) {
                return true;
            }
            nbs.add(nums[i]);
        }

        return false;
    }
}
