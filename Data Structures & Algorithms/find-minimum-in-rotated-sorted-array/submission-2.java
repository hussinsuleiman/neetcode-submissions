class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length-1;
        int mid = 0;
        int min = nums[0];

        while (start < end) {
            mid = (start+end) / 2;

            if (nums[mid] >= nums[0]) {
                min = Math.min(nums[0], min);
                start = mid + 1;
            }
            else {
                min = Math.min(nums[mid], min);
                end = mid - 1;
            }
        }

        return Math.min(nums[start], min);   
    }
}
