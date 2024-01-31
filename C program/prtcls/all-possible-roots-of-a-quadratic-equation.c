#include<stdio.h>
#include<math.h>
main()
{
int a,b,c,d;
float x1,x2;
printf("Input a,b,c\n");
scanf("%d%d%d",&a,&b,&c);
d=b*b-(4*a*c);
if(d==0)
{
printf("The roots are real and equal\n");
x1=-b/(2*a);
printf("x1=%f x2=%f",x1,x1);
}
else if(d>0)
{
printf("The roots are real & unequal\n");
x1=(-b+sqrt(d))/(2*a);
x2=(-b-sqrt(d))/(2*a);
printf("x1=%f x2=%f",x1,x2);
}
else
{
printf("The roots are Imajinary");
}
}
