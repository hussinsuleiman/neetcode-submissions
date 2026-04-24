class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0;
        int j = 0;
        int l1 = s.size();
        int l2 = t.size();

        while (j < l2) {
            if (t[j] == s[i]) {
                i++;
            }

            if (i == l1) {
                return true;
            }
            
            j++;
        }

        return false;
    }
};