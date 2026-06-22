class Solution {
    public List<List<Integer>> permutations(int[] nums, int k) {
        List<List<Integer>> perm = new ArrayList<>();
        ArrayList<Integer> numArray = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            numArray.add(nums[i]);
        }

        if (k == 0) {
            perm.add(numArray);
            return perm;
        }

        List<List<Integer>> permPrev = permute(Arrays.copyOfRange(nums, 0, k));

        for (List<Integer> l : permPrev) {
            for (int i = k; i >= 0; i--) {
                l.add(i, nums[k]);
                perm.add(new ArrayList(l));
                l.remove(i);
            }
        }

        return perm;
    }

    public List<List<Integer>> permute(int[] nums) {
        return permutations(nums, nums.length-1);        
    }
}
