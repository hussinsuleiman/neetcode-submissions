class Solution {
    public void backtrack(List<List<Integer>> res, int[] nbs, List<Integer> sub, int i) {        
        if (i == nbs.length) {
            res.add(new ArrayList<>(sub));
            return;
        }
        
        sub.add(nbs[i]);
        backtrack(res, nbs, sub, i+1);
        sub.remove(sub.size()-1);
        backtrack(res, nbs, sub, i+1);
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        backtrack(result, nums, subset, 0);
        return result;
    }
}
