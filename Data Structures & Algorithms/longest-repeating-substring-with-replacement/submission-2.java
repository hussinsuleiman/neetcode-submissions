class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> count = new HashMap<>();
        int result = 0;
        int len = s.length();
        int l = 0;
        int maxCount = 0;

        for (int r = 0; r < len; r++) {
            if (count.containsKey(s.charAt(r))) {
                count.put(s.charAt(r), count.get(s.charAt(r))+1);
            }
            else {
                count.put(s.charAt(r), 1);
            }

            maxCount = Math.max(maxCount, count.get(s.charAt(r)));

            while (r-l+1 - maxCount > k) {
                count.put(s.charAt(l), count.get(s.charAt(l))-1);
                maxCount = Math.max(maxCount, count.get(s.charAt(r))); 
                l++;
            }

            result = Math.max(r-l+1, result);
        }

        return result;
    }
}
