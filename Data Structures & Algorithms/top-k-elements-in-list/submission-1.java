class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> occ = new HashMap<>();
        int[] output = new int[k];

        for (int i = 0; i < nums.length; i++) {
            if (occ.containsKey(nums[i])) {
                occ.put(nums[i], occ.get(nums[i]) + 1);
            }
            else {
                occ.put(nums[i], 1);
            }
        }

        ArrayList<ArrayList<Integer>> freqGroups = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i < nums.length; i++) {
            ArrayList<Integer> entry = new ArrayList<Integer>();
            freqGroups.add(entry);
        }

        for (Integer n : occ.keySet()) {
            freqGroups.get(occ.get(n)-1).add(n);
        }

        int totalReturned = 0;
        int j = nums.length-1;

        while (totalReturned < k) {
            for (Integer n : freqGroups.get(j)) {
                output[totalReturned] = n;
                totalReturned++;
            }
            j--; 
        }

        return output;
    }
}
