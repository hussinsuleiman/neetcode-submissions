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

    public List<List<String>> groupAnagrams(String[] strs) {
        boolean[] chosen = new boolean[strs.length];
        List<List<String>> output = new ArrayList<List<String>>();

        for (int i = 0; i < strs.length; i++) {
            if (!chosen[i]) {
                ArrayList<String> l = new ArrayList<>();
                l.add(strs[i]);
                chosen[i] = true;
                for (int j = i+1; j < strs.length; j++) {
                    if (isAnagram(strs[i], strs[j])) {
                        l.add(strs[j]);
                        chosen[j] = true;
                    }
                }

                output.add(l);
            }
        }

        return output;
    }
}
