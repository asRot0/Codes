#include<stdio.h>
#include<math.h>
main()
{
float a,b,c,s,ar;
printf("enter a, b, c");
scanf("%f%f%f",&a,&b,&c);
s=(a+b+c)/2;
ar=sqrt(s*(s-a)*(s-b)*(s-c));
printf("AREA=%f\n",ar);
}
