#include<stdio.h>
main()
{
int x=0,y=1,z,n,i;
printf("How Many Number: ");
scanf("%d",&n);
printf("\nFibonacci Number\n");
printf("0 1");
for(i=0; i<n-2; i++)
{
printf(" %d",x+y);
z=y;
y=x+y;
x=z;
}
}
