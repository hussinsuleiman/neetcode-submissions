#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        
        if (i%2 == 0) {
            cout << s << "\n";
        }
    } 
}