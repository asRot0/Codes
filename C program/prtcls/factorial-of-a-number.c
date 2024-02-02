#include<stdio.h>
#include<math.h>
main()
{
int n,i,s=1;
printf("Enter the number : ");
scanf("%d",&n);
i=1;
while(i<=n)
{
s=s*i;
i=i+1;
}
printf("The factorial value of the number : %d",s);
}
