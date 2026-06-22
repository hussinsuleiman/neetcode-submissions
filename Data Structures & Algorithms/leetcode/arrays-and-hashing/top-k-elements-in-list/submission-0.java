class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<List<Integer>> buckets = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            ArrayList<Integer> nbs = new ArrayList<>();
            buckets.add(nbs);
        }
        HashMap<Integer, Integer> occ = new HashMap<>();
        int[] output = new int[k];
        int index = 0;

        for (int i = 0; i < nums.length; i++) {
            if (occ.containsKey(nums[i])) {
                occ.put(nums[i], occ.get(nums[i])+1);
            }
            else {
                occ.put(nums[i], 1);
            }
        }

        for (int nb : occ.keySet()) {
            buckets.get(occ.get(nb)-1).add(nb);
        }

        for (int i = nums.length-1; i >= 0; i--) {
            for (int nb : buckets.get(i)) {
                if (index < k) {
                    output[index] = nb;
                    index++;
                }
            }
        }

        return output;
    }
}
