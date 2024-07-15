#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    string num_word[11] = {"even","odd","one","two","three","four","five","six","seven","eight","nine"};
    for(int i = a; i <= b; i++ ){
        if(i >= 1 && i <= 9){
            cout << num_word[i+1] << endl;
        }else{

            cout << num_word[i%2] << endl;
        }
    }
    return 0;
}