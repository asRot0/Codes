#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {

    int n, s, p, q;
    std::cin >> n >> s >> p >> q;

    std::vector<int> a(n);
    a[0] = s ;

    for (int i = 1; i < n ;i++ ) {
        a[i] = (a[i - 1] * p) + q;
    }
    int count = 1;

    for (int i = 0; i < n-1; i++) {

        if (a[i] != a[i + 1]) {
            count++;
        }
    }
    std::cout << count;

    return 0;
}