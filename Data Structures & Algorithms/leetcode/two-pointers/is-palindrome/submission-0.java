class Solution {
    public boolean isAlphaNum(char c) {
        return ('a' <= c && c <= 'z') || ('0' <= c && c <= '9');
    }
    
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int len = s.length();
        int i = 0;
        int j = len-1;

        while (i < j) {
            char letterI = s.charAt(i);
            char letterJ = s.charAt(j);

            if (!isAlphaNum(letterI)) {
                i++;
            }
            if (!isAlphaNum(letterJ)) {
                j--;
            }
            if (isAlphaNum(letterI) && isAlphaNum(letterJ)) {
                if (letterI != letterJ) {
                    return false;
                }
                i++;
                j--;
            }
        }
        
        return true;
    }
}
