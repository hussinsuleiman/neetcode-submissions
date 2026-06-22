class Solution {
    public void backtrack(List<List<Integer>> res, int[] nbs, List<Integer> sub, int tar, int currSum, int i) {
        if (currSum == tar) {
            res.add(new ArrayList<>(sub));
            return;
        }
        if (currSum > tar || i == nbs.length) {
            return;
        }

        sub.add(nbs[i]);
        currSum += nbs[i];
        backtrack(res, nbs, sub, tar, currSum, i);
        currSum -= sub.get(sub.size()-1);
        sub.remove(sub.size()-1);
        backtrack(res, nbs, sub, tar, currSum, i+1);
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        backtrack(result, nums, subset, target, 0, 0);
        return result; 
    }
}
