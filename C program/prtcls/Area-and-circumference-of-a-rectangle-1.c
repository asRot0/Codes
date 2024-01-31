#include<stdio.h>
main()
{
float a,b,area,cir;
printf("LENGTH and WIDTH: ");
scanf("%f %f",&a,&b);
area=a*b;
cir=2*(a+b);
printf("AREA=\n%f CIRCUMFERENCE=\n%f",area,cir);
}
