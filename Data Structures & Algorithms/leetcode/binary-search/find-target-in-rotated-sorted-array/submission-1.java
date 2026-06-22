class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length-1;
        int mid = 0;
        int indexMin = 0;

        while (start < end) {
            mid = (start+end) / 2;

            if (nums[mid] >= nums[0]) {
                if (nums[0] < nums[indexMin]) {
                    indexMin = 0;
                }
                start = mid + 1;
            }
            else {
                if (nums[mid] < nums[indexMin]) {
                    indexMin = mid;
                }
                end = mid - 1;
            }
        }
        
        if (nums[start] < nums[indexMin]) {
            indexMin = start;
        }

        return indexMin;   
    }

    public int search(int[] nums, int target) {
        int start = findMin(nums);
        int end = start + nums.length - 1;
        int mid = 0;

        while (start <= end) {
            mid = ((start+end) / 2);

            if (nums[mid % nums.length] == target) {
                return mid % nums.length;
            }
            else if (nums[mid % nums.length] > target) {
                end = mid-1;
            }
            else {
                start = mid+1;
            }
        }

        return -1;
    }
}
