#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int C, n;
    
    while (cin >> C >> n) {
        vector<int> values(n), weights(n);
    
        for (int i = 0; i < n; i++) {
            cin >> values[i] >> weights[i];
        }
        
        vector<int> dp(C+1, 0);
        vector<vector<bool>> keep(n, vector<bool>(C+1, false));
        
        for (int i = 0; i < n; i++) {
            int v = values[i];
            int w = weights[i];
            
            for (int j = C; j >= w; j--) {
                if (dp[j-w] + v > dp[j]) {
                    dp[j] = dp[j-w] + v;
                    keep[i][j] = true;
                }
            }
        }
        
        int best_w = 0;
        
        for (int j = 1; j <= C; j++) {
            if (dp[j] > dp[best_w]) {
                best_w = j;
            }
        }
        
        vector<int> selected_items;
        int current_w = best_w;
        
        for (int i = n-1; i >= 0; i--) {
            if (keep[i][current_w]) {
                selected_items.push_back(i);
                current_w -= weights[i];
            }
        } 
        
        cout << selected_items.size() << "\n";
        
        for (int i = selected_items.size()-1; i >= 0 ; i--) {
            cout << selected_items[i];
            
            if (i > 0) {
                cout << " ";
            }
        }
        
        cout << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}