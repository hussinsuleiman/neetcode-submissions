class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        vector<int> res(n, -1);
        int curMax = arr[n-1];

        for (int i = n-2; i >= 0; i--) {
            res[i] = curMax;
            
            if (arr[i] > curMax) {
                curMax = arr[i];
            }
        }

        return res;
    }
};