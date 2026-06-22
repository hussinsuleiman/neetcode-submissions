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
}
