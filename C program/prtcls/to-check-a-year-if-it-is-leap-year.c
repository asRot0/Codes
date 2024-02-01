#include<stdio.h>
main()
{
int a;
printf("Enter year: ");
scanf("%d",&a);
if ((a%400==0)||(a%100!=0&&a%4==0))
printf("%d is leap year.",a);
else
printf("%d is not leap year.",a);
getch();
}
