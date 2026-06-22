class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);
        int maxCons = 1;
        int lastInt = nums[0];
        int cons = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == lastInt+1) {
                cons++;
                lastInt++;
            }
            else if (nums[i] != lastInt) {
                if (cons > maxCons) {
                    maxCons = cons;
                }

                cons = 1;
                lastInt = nums[i];
            }
        }

        if (cons > maxCons) {
            maxCons = cons;
        }

        return maxCons;
    }
}
