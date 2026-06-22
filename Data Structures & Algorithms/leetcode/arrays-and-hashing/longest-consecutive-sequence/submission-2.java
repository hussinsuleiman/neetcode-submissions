class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        HashSet<Integer> nbs = new HashSet<>();
        HashSet<Integer> possibleStart = new HashSet<>();
        int cons = 1;
        int maxCons = 1;

        for (int i = 0; i < nums.length; i++) {
            if (!nbs.contains(nums[i])) {
                nbs.add(nums[i]);
            }
        }

        for (int nb : nbs) {
            if (!nbs.contains(nb-1)) {
                possibleStart.add(nb);
            }
        }

        for (int num : possibleStart) {
            while (nbs.contains(num+1)) {
                num++;
                cons++;
            }
            if (cons > maxCons) {
                maxCons = cons;
            }
            cons = 1;
        }

        return maxCons;
    }
}
