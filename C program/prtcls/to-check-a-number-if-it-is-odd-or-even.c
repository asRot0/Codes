#include<stdio.h>
main()
{
int n,r;
printf("Number: ");
scanf("%d",&n);
r=n%2;//here we have used "%"to find the remainder.
if (r==0)
printf("%d is even",n);
else
printf("%d is odd",n);
getch();
}
