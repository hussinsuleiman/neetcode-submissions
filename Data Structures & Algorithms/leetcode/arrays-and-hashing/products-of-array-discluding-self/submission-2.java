class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        prefix[0] = 1;
        suffix[nums.length-1] = 1;

        for (int i = 0; i < nums.length-1; i++) {
            prefix[i+1] = prefix[i] * nums[i];
        }

        for (int j = nums.length-1; j > 0; j--) {
            suffix[j-1] = suffix[j] * nums[j];
        }

        int[] products = new int[nums.length];

        for (int k = 0; k < nums.length; k++) {
            products[k] = prefix[k] * suffix[k];
        }

        return products;
    }
}  
