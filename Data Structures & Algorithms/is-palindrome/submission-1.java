class Solution {
    public boolean isAlphaNum(char c) {
        return ('a' <= c && c <= 'z') || ('0' <= c && c <= '9');
    }

    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;
        s = s.toLowerCase();

        while (l < r) {
            char atL = s.charAt(l);
            char atR = s.charAt(r);

            if (!isAlphaNum(atL)) {
                l++;
            }
            else if (!isAlphaNum(atR)) {
                r--;
            }
            else if (atL != atR) {
                return false;
            }
            else {
                l++;
                r--;
            }
        }

        return true;
    }
}
