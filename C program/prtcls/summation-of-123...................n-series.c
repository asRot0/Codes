#include<stdio.h>
main()
{
int n,i,s=0;
printf("Last value : ");
scanf("%d",&n);
for(i=1;i<=n;i=i+1)
s=s+i;
printf("sum : %d",s);
}
