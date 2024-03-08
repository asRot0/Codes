#include <stdio.h>

void swap(int *i,int *j)
{
    int temp;
    temp=*i;
    *i=*j;
    *j=temp;
}

int main(void)
{
    int num1,num2;
    printf("enter number1 & number2:");
    scanf("%d%d",&num1,&num2);
    printf("number1: %d number2: %d\n",num1,num2);
    swap(&num1,&num2);
    printf("number1: %d number2: %d\n",num1,num2);

    return 0;
}
