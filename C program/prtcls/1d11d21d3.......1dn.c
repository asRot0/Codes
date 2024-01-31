#include<stdio.h>
main()
{
int n;
float s=0.0,i;
printf("N : ");
scanf("%d",&n);
for(i=1;i<=n;i++)
{
s=s+(1/i);
}
printf("Ans : %f",s);
}
