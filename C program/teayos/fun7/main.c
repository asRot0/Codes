#include<stdio.h>

void f1(int num[5]), f2(int num[ ]), f3(int *num);

int main(void)
{
    int count[5]={1,2,3,4,5};
    f1(count);
    f2(count);
    f3(count);

    return 0;
}

void f1(int num[5])
{
    for(int i=0;i<5;i++) printf(" %d",num[i]);
}

void f2(int num[ ])
{
    for(int i=0;i<5;i++) printf(" %d",num[i]);
}

void f3(int *num)
{
    for(int i=0;i<5;i++) printf(" %d",num[i]);
}
