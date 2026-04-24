class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length();
        int len2 = s2.length();

        if (len2 < len1) {
            return false;
        }

        HashMap<Character, Integer> occ = new HashMap<>();
        int start = 0;

        for (int i = 0; i < len1; i++) {
            if (occ.containsKey(s1.charAt(i))) {
                occ.put(s1.charAt(i), occ.get(s1.charAt(i))+1);
            }
            else {
                occ.put(s1.charAt(i), 1);
            }
            if (occ.containsKey(s2.charAt(i))) {
                occ.put(s2.charAt(i), occ.get(s2.charAt(i))-1);
            }
            else {
                occ.put(s2.charAt(i), -1);
            }
        }

        while (start + len1 <= len2) {
            boolean is_perm = true;

            for (int nb: occ.values()) {
                if (nb != 0) {
                    is_perm = false;
                    break;
                }
            }

            if (is_perm) {
                return true;
            }
            if (start+len1 < len2) {
                occ.put(s2.charAt(start), occ.get(s2.charAt(start))+1);
                if (occ.containsKey(s2.charAt(start+len1))) {
                    occ.put(s2.charAt(start+len1), occ.get(s2.charAt(start+len1))-1);
                }
                else {
                    occ.put(s2.charAt(start+len1), -1);
                }
            }
            start++;
        }

        return false;
    }
}
