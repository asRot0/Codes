class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        int t = low;
        int n = 0;
        while (t > 0) {
            t = t / 10;
            ++n;
        }

        int start = 0;
        int increment = 0;
        for (int i = 1; i <= n; ++i) {
            start = start * 10 + i;
            increment = increment * 10 + 1;
        }

        int num = start;
        vector<int> res;
        while (num <= high) {
            for (int i = 0; i < (10 - n); ++i) {
                if (num >= low && num <= high) {
                    res.push_back(num);
                }
                num += increment;
            }
            ++n;
            increment = increment * 10 + 1;
            num = start * 10 + n;
            start = num;
        }
        return res;
    }
};