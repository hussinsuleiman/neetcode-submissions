class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> occT = new HashMap<>();
        HashMap<Character, Integer> occS = new HashMap<>();
        HashSet<Character> charsInT = new HashSet<>();
        int l = 0;
        int r = 0;
        int[] indicesResult = new int[2];
        indicesResult[1] = s.length()-1;
        boolean foundSubstring = false;
        int have = 0;

        for (int i = 0; i < t.length(); i++) {
            if (occT.containsKey(t.charAt(i))) {
                occT.put(t.charAt(i), occT.get(t.charAt(i))+1);
            }
            else {
                occT.put(t.charAt(i), 1);
                charsInT.add(t.charAt(i));
            }
        }

        int need = charsInT.size();

        while (r < s.length()) {
            if (charsInT.contains(s.charAt(r))) {
                if (occS.containsKey(s.charAt(r))) {
                    occS.put(s.charAt(r), occS.get(s.charAt(r))+1);
                }
                else {
                    occS.put(s.charAt(r), 1);
                }

                if (occS.get(s.charAt(r)) == occT.get(s.charAt(r))) {
                    have++;
                }
            }

            if (have == need) {
                foundSubstring = true;
            }

            while (have == need) {
                if (charsInT.contains(s.charAt(l))) {
                    occS.put(s.charAt(l), occS.get(s.charAt(l))-1);
                    if (occS.get(s.charAt(l)) < occT.get(s.charAt(l))) {
                        if (r-l <= indicesResult[1]-indicesResult[0]) {
                            indicesResult[0] = l;
                            indicesResult[1] = r+1;
                        }

                        have--;
                    } 
                }

                l++;       
            }

            r++;
        }

        if (foundSubstring) {
            return s.substring(indicesResult[0], indicesResult[1]);
        }
        
        return "";
    }   
}
