#include<iostream>
using namespace std;

int i, n, a[20];
void getInput() {
    cout<<"Enter the Numbers: ";
    for(i=0; i<n; i++) {
        cin>>a[i];
    }
}

void show() {
    cout<<"Input Data: ";
    for(i=0; i<n; i++) {
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

void bubbleSort() {
    int temp, j;
    cout<<endl;
    cout<<"Before Sorting: ";
    for(i=0; i<n; i++) {
        cout<<a[i]<<" ";
    }
    cout<<endl;
    for(i=0; i<n; i++) {
        for(j=i+1; j<n; j++) {
            if(a[i]>a[j]) {
                temp = a[i];
                a[i]= a[j];
                a[j] = temp;
            }
        }
    }
    cout<<"After Sorting: ";
    for(i=0; i<n; i++) {
        cout<<a[i]<<" ";
    }
    cout<<endl<<endl;
}

int main() {
    cout<<"Binary Search Program." <<endl;
    cout<<"How many numbers do you want to input: ";
    cin>>n;
    getInput();
    show();
    bubbleSort();

    return 0;
}

