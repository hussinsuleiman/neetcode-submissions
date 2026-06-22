class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> letterIndex = new HashMap<>();
        int result = 0;
        int l = 0;

        for (int i = 0; i < s.length(); i++) {
            if (letterIndex.containsKey(s.charAt(i))) {
                l = Math.max(l, letterIndex.get(s.charAt(i))+1);
            }
            letterIndex.put(s.charAt(i), i);
            result = Math.max(result, i-l+1);
        }

        return result;
    }
}
