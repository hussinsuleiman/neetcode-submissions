class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> occ(26, 0);
        int l1 = s.size();
        int l2 = t.size();

        if (l1 != l2) {
            return false;
        }

        for (int i = 0; i < l1; i++) {
            occ[s[i]-'a'] += 1;
            occ[t[i]-'a'] -= 1;
        }

        for (int i = 0; i < 26; i++) {
            if (occ[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
};
