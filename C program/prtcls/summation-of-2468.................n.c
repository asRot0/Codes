#include<stdio.h>
main()
{
int n,i,s=0;
printf("Last value : ");
scanf("%d",&n);
i=0;
while(i<=n)
{
s=s+i;
i=i+2;
}
printf("sum : %d",s);
}
