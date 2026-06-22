class Solution {
    public void countChars(String a, char[] l) {
        int x = a.length();

        for (int i = 0; i < x; i++) {
            l[a.charAt(i)-'a']++;
        }
    }

    public boolean isAnagram(String s, String t) {
        char[] charsOfS = new char[26];
        char[] charsOfT = new char[26];
    
        countChars(s, charsOfS);
        countChars(t, charsOfT);

        for (int i = 0; i < 26; i++) {
            if (charsOfS[i] != charsOfT[i]) {
                return false;
            }
        }

        return true;
    }
    
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<List<String>>();

        for (int i = 0; i < strs.length; i++) {
            boolean isNewGroup = true;

            for (int j = 0; j < output.size(); j++) {
                if (isAnagram(strs[i], output.get(j).get(0))) {
                    output.get(j).add(strs[i]);
                    isNewGroup = false;
                    break;
                }
            }

            if (isNewGroup) {
                ArrayList<String> newList = new ArrayList<>();
                newList.add(strs[i]);
                output.add(newList);
            }
        }

        return output;
    }
}
