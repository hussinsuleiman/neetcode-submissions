class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        int r = 1;
        int maxLen = 1;
        int maxFreq = 1;
        HashMap<Character, Integer> occ = new HashMap<>();
        occ.put(s.charAt(0), 1); 
        int sLen = s.length();

        while (r < sLen) {
            char atR = s.charAt(r);
            
            if (occ.containsKey(atR)) {
                int newOcc = occ.get(atR) + 1;
                occ.put(atR, newOcc);
                maxFreq = Math.max(maxFreq, newOcc);
            }
            else {
                occ.put(atR, 1);
            }

            if (r-l+1 <= maxFreq + k) {
                maxLen = Math.max(maxLen, r-l+1);
            }
            else {
                occ.put(s.charAt(l), occ.get(s.charAt(l))-1);
                l++;
            }

            r++;
        }

        return maxLen;
    }
}
