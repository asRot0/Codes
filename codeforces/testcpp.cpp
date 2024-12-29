#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;

        vector<int> a(m);
        unordered_set<int> known_set;

        for (int i = 0; i < m; i++) {
            cin >> a[i];
        }

        for (int i = 0; i < k; i++) {
            int q;
            cin >> q;
            known_set.insert(q);
        }

        string res = "";

        for (int i = 0; i < m; i++) {
            if (known_set.find(a[i]) == known_set.end()) {
                res += '1';
            } else {
                res += '0';
            }
        }

        cout << res << endl;
    }

    return 0;
}
