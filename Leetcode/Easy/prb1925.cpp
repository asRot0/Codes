class Solution {
public:
    int countTriples(int n) {
        int count = 0;
        int limit = n*n;
        for (int i=1; i<=n; i++){
            for (int j=1; j<=n; j++){
                int k = i*i + j*j;
                if (k > limit) break;
                if (sqrt(k) == (int)sqrt(k))
                    count++;
            }
        }
        return count;
    }
};