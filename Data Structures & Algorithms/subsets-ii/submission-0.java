class Solution {
    public void backtrack(List<List<Integer>> res, int[] nbs, List<Integer> cur, int i) {
        if (i == nbs.length) {
            res.add(new ArrayList(cur));
            return;
        }
        
        cur.add(nbs[i]);
        backtrack(res, nbs, cur, i+1);
        cur.remove(cur.size()-1);

        while (i+1 < nbs.length && nbs[i] == nbs[i+1]) {
            i++;
        }
        backtrack(res, nbs, cur, i+1);
    }
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(result, nums, current, 0);
        return result;
    }
}
