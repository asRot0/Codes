#include<stdio.h>
main()
{
int y;
float x,z;
printf("Floating Point Number: ");
scanf("%f",&x);
y=(int)x;
z=x-y;
printf("Integer Part: %d\n",y);
printf("Floating Part: %f",z);
getch();
}
