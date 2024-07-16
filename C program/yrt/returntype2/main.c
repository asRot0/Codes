#include <stdio.h>
#include <conio.h>
int get_sqr(void);
int main()
{
    int sqr;
    sqr =  get_sqr();
    printf("Square of the number is %d",sqr);
    getch();
    return 0;
}
int get_sqr(void)
{
    int num;
    printf("Enter a number:");
    scanf("%d",&num);
    return num*num;
}
