#include<stdio.h>
main()
{
int n;
printf("Number: ");
scanf("%d",&n);
if (n%5==0)
printf("%d is dividable by 5",n);
else
printf("%d isn't dividable by 5",n);
getch();
}
