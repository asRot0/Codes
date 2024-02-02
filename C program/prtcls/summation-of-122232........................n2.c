#include<stdio.h>
#include<math.h>
main()
{
int n,i,s=0;
printf("Last value : ");
scanf("%d",&n);
i=1;
while(i<=n)
{
s=s+pow(i,2);
i=i+1;
}
printf("sum : %d",s);
}
