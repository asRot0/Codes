#include<stdio.h>
main()
{
int a;
printf("Enter year: ");
scanf("%d",&a);
if (a%400==0)
printf("%d is leap year.",a);
else
{
    if ((a%100!=0)&&(a%4==0))
    printf("%d is a leap year",a);
    else
    printf("%d in not a leap year",a);
}
}
