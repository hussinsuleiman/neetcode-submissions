class Solution {
    public int lengthOfLongestSubstring(String s) {
        int sLen = s.length();

        if (sLen == 0) {
            return 0;
        }

        int maxLen = 1;
        int startSeq = 0;
        HashMap<Character, Integer> charsInSeq = new HashMap<>();
        charsInSeq.put(s.charAt(0), 0);
        int i = 1;
        int len = 1;

        while (i < sLen) {
            if (charsInSeq.containsKey(s.charAt(i))) {
                if (len > maxLen) {
                    maxLen = len;
                }
                startSeq = Math.max(startSeq, charsInSeq.get(s.charAt(i)) + 1);
                len = i - startSeq + 1;
            }
            else {
                len++;
            }

            charsInSeq.put(s.charAt(i), i);
    	    i++;
        }
        
        return Math.max(maxLen, len);
    }
}
