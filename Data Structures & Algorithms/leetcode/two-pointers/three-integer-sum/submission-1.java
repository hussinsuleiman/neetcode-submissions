class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        int i = 0;
        int l = 0;
        int r = 0;

        while (i < nums.length) {
            l = i+1;
            r = nums.length-1;

            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    ArrayList<Integer> outputList = new ArrayList<>();
                    outputList.add(nums[i]);
                    outputList.add(nums[l]);
                    outputList.add(nums[r]);
                    output.add(outputList);
                    while (l < nums.length-1 && nums[l+1] == nums[l]) {
                        l++;
                    }  
                    l++;
                    while (r > 0 && nums[r-1] == nums[r]) {
                        r--;
                    } 
                    r--;
                }
                else if (nums[i] + nums[l] + nums[r] < 0) {
                    l++;
                } 
                else {
                    r--;
                }
            }

            while (i < nums.length-1 && nums[i+1] == nums[i]) {
                i++;
            }
            i++;
        }

        return output;
    }
}
