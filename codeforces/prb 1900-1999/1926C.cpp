#include <iostream>
#include <string>

using namespace std;

int digit_sum(int n) {
    if (n < 10) {
        return n * (n + 1) / 2;
    }

    string n_str = to_string(n);
    int digits = n_str.length();
    int power_of_10 = 1;
    for (int i = 1; i < digits; ++i) {
        power_of_10 *= 10;
    }
    int first_digit = n / power_of_10;

    int result = digit_sum(first_digit - 1) * power_of_10;
    result += first_digit * (n % power_of_10 + 1);
    result += first_digit * digit_sum(power_of_10 - 1);
    result += digit_sum(n % power_of_10);

    return result;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << digit_sum(n) << endl;
    }
    return 0;
}

