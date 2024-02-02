#include<stdio.h>
main()
{
int n,r;
printf("Number: ");
scanf("%d",&n);
if ((n%2==0)&&(n%5==0))
printf("%d is dividable by 2 and 5",n);
else
printf("%d isn't dividable by 2 and 5",n);
getch();
}
