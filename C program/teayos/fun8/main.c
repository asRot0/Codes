#include<stdio.h>

void prompt(char *msg,int *num);

int main(void)
{
    int i;
    prompt("enter a num:",&i);
    printf("your number is : %d",i);

    return 0;
}

void prompt(char *msg,int *num)
{
    printf(msg);
    scanf("%d",num); //num is already a pointer, do not need to precede
}
