class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> nbs = new HashSet<>();

        for (int nb : nums) {
            if (nbs.contains(nb)) {
                return true;
            }
            nbs.add(nb);
        }

        return false;
    }
}
