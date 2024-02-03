class Solution {
public:
    int countDigits(int num) {
        int c = num;
        int res = 0;
        while(c > 0){
            if(num % (c % 10) == 0) res++;
            c /= 10;
        }
        return res;
    }
};