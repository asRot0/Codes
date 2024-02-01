#include<stdio.h>
main()
{
float f,c;
printf("Input Celsius: ");
scanf("%f",&c);
f=(9*c)/5+32;
printf("Fahrenheit: %.2f",f);//here we have used ".2" to show how many digits there will be after decimal point.
//we can use here "getch()"
}

