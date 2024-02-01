#include<stdio.h>
main()
{
long int a,r,s=0;
printf("integer input= ");
scanf("%ld",&a);//"%ld" = long int
printf("\nreverse form= ");
while(a!=0)
{
r=a%10;
printf("%ld",r);
s=s+r;
a=a/10;
}
printf("\nsum= %ld", s);
}
