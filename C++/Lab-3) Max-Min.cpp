#include<iostream>
using namespace std;

int maxmin (int a[], int left, int right, int &max, int &min) {
    int max1,min1,mid;
    if(left==right) {
        max=min=a[left];
    }
    else if(left == right - 1) {
        if(a[left] > a[right]) {
            max = a[left];
            min = a[right];
        } else {
            max = a[right];
            min = a[left];
        }
    }
    else {
        mid = (left+right) / 2;
        maxmin(a,left,mid,max,min);
        maxmin(a,mid+1,right,max1,min1);
        if(max1>max) {
            max=max1;
        }
        if(min1<min) {
            min = min1;
        }
    }
    return 0;
}

int main() {
    int a[20],i,n,max,min;
    cout<<"Enter the Length of the Array: ";
    cin>>n;
    cout<<"Enter the Elements: ";
    for (int i = 0; i < n; i++){
        cin>>a[i];
    }
    maxmin(a, 0, n - 1, max, min);
    cout<<endl<<endl;
    cout<<"Maximum element in the array = "<<max<<endl;
    cout<<"Minimum element in the array = "<<min<<endl;

}
