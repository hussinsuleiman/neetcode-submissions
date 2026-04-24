class Solution {
    public boolean isAnagram(String s, String t) {
        int lenS = s.length();
        int lenT = t.length();

        if (lenS != lenT) {
            return false;
        }

        HashMap<Character, Integer> occ = new HashMap<>();

        for (int i = 0; i < lenS; i++) {
            char letter = s.charAt(i);

            if (occ.containsKey(letter)) {
                occ.put(letter, occ.get(letter)+1);
            }
            else {
                occ.put(letter, 1);
            }
        }

        for (int i = 0; i < lenT; i++) {
            char letter = t.charAt(i);

            if (occ.containsKey(letter)) {
                occ.put(letter, occ.get(letter)-1);
            }
            else {
                return false;
            }
        }

        for (char key : occ.keySet()) {
            if (occ.get(key) != 0) {
                return false;
            }
        }

        return true;
    }
}
