#include<iostream>
using namespace std;

int i, n, a[20], comparisons;
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
    int temp, j, index;
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

int binarySearch(int x, int a[],int n) {
    int low=0, high=n-1, mid, found=0;
    comparisons=0;
    while((low<=high) && (!found)) {
        mid=(low+high)/2;
        comparisons++;
        if(x<a[mid]) {
            high = mid-1;
        } else if(x > a[mid]) {
            low = mid +1;
        } else {
            found = 1;
        }
    }

    if(found)
        return mid;
    else
        return -1;
}

int main() {
    int item,x;
    cout<<"Binary Search Program." <<endl;
    cout<<"How many numbers do you want to input: ";
    cin>>n;
    getInput();
    show();
    bubbleSort();

    cout<<"Which Number to be searched: ";
    cin>> x;

    item = binarySearch(x,a,n);
    if(item == -1)
        cout<<"Item Not Found\n";
    else
        cout<<"Item Found"<<endl;

    cout<<"Total Comparisons: "<<comparisons;

    return 0;
}


