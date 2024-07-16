#include <stdio.h>
int main()
{
float F,C,K;
printf("Enter the Celsius temperature:");
scanf("%f",&C);
F=(9*C)/5+32;
printf("Fahrenheit temperature is=%.2f",F);
printf("\nEnter the Kelvin temperature:");
scanf("%f",&K);
F=(((K-273)*9)/5)+32;
printf("Fahrenheit temperature is=%.2f",F);
printf("\nTHANK YOU FOR USE MY PROGRAM...");
    return 0;
}
