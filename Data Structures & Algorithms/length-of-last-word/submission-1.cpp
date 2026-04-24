class Solution {
public:
    int lengthOfLastWord(string s) {
        int l = s.size();
        int i = l-1;

        while (s[i] == ' ') {
            i--;
        }

        int res = 0;

        while (i >= 0 and s[i] != ' ') {
            res++;
            i--;
        }

        return res;
    }
};