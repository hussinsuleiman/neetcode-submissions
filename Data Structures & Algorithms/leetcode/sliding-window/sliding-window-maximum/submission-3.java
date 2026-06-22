class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        HashMap<Integer, ArrayList<Integer>> nbsToIndices = new HashMap<>();
        int[] output = new int[nums.length-k+1];
        boolean[] filled = new boolean[nums.length-k+1];

        for (int i = 0; i < nums.length; i++) {
            if (nbsToIndices.containsKey(nums[i])) {
                nbsToIndices.get(nums[i]).add(i);
            }
            else {
                ArrayList<Integer> indices = new ArrayList<>();
                indices.add(i);
                nbsToIndices.put(nums[i], indices);
            }
        }
        
        Arrays.sort(nums);
        int indexMax = nums.length-1;
        
        while (indexMax >= 0) {
            ArrayList<Integer> indicesMax = nbsToIndices.get(nums[indexMax]);

            for (Integer i : indicesMax) {
                for (int j = i-k+1; j <= i; j++) {
                    if (0 <= j && j <= nums.length-k && !filled[j]) {
                        output[j] = nums[indexMax];
                        filled[j] = true;
                    }
                }
            }

            indexMax--;
        }

        return output;
    }
}
