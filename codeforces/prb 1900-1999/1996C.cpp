#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;
        string a, b;
        cin >> a >> b;

        vector<vector<int>> prefix_a(n + 1, vector<int>(26, 0));
        vector<vector<int>> prefix_b(n + 1, vector<int>(26, 0));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < 26; ++j) {
                prefix_a[i + 1][j] = prefix_a[i][j];
                prefix_b[i + 1][j] = prefix_b[i][j];
            }
            prefix_a[i + 1][a[i] - 'a']++;
            prefix_b[i + 1][b[i] - 'a']++;
        }

        while (q--) {
            int l, r;
            cin >> l >> r;
            l--; r--;

            vector<int> count_a(26, 0);
            vector<int> count_b(26, 0);

            for (int i = 0; i < 26; ++i) {
                count_a[i] = prefix_a[r + 1][i] - prefix_a[l][i];
                count_b[i] = prefix_b[r + 1][i] - prefix_b[l][i];
            }

            int changes_needed = 0;
            for (int i = 0; i < 26; ++i) {
                if (count_a[i] < count_b[i]) {
                    changes_needed += count_b[i] - count_a[i];
                }
            }

            cout << changes_needed << endl;
        }
    }
    return 0;
}