#include<stdio.h>
#define pi 3.1416
main()
{
float r,area,cir;
printf("RADIUS: ");
scanf("%f",&r);
area=pi*r*r;
cir=2*pi*r;
printf("AREA=\n%f",area);
printf(" CIRCUMFERENCE=\n%f",cir);
}
