#include <stdio.h>
#include <conio.h>
int fact(long n);
int main(void)
{
    long num, f ;
    printf("Enter a number:");
    scanf("%ld",&num);
    f=fact(num);
    printf("The factorial is %ld",f);
    getch();
}
int fact(long n)
{
    if (n==0)
        return 1;
    else
        return(n*fact(n-1));
}
