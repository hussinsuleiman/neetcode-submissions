class Solution {
    public int[] productExceptSelf(int[] nums) {
        int productNonZero = 1;
        ArrayList<Integer> zeroesIndices = new ArrayList<>();
        int[] output = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                zeroesIndices.add(i);
            }
            else {
                productNonZero *= nums[i];
            }
        }

        if (zeroesIndices.size() >= 2) {
            return output;
        }

        if (zeroesIndices.size() == 1) {
            output[zeroesIndices.get(0)] = productNonZero;
            return output;
        }

        for (int i = 0; i < nums.length; i++) {
            output[i] = productNonZero/nums[i];
        }

        return output;
    }
}  
