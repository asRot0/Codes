#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll t;
    cin >> t;
    while(t--){
        ll x;
        cin >> x;
        ll cow, hen;
        cow = x/4;
        hen = (x%4)/2;
        cout << cow+hen << endl;
    }
    return 0;
}