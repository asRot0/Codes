#include <stdio.h>
int main()
{

float C,F,K;
printf("Temperature sequence .Celsius\n                     .Fahrenheit\n                     .Kelvin");
printf("\nEnter the Celsius Temperature:");
scanf("%f",&C);
F=(9*C)/5+32;
K=((C*5)/5)+273;
printf("Fahrenheit Temperature is=%.2f",F);
printf("\nKelvin Temperature is=%.2f",K);
printf("\nEnter the Fahrenheit Temperature:");
scanf("%f",&F);
C=((F-32)/9)*5;
K=(((F-32)/9)*5)+273;
printf("Celsius Temperature is=%.2f",C);
printf("\nKelvin Temperature is=%.2f",K);
printf("\nEnter the Kelvin Temperature:");
scanf("%f",&K);
C=((K-273)/5)*5;
F=(((K-273)/5)*9)+32;
printf("Celsius Temperature is=%.2f",C);
printf("\nFahrenheit Temperature is=%.2f",F);
printf("\nTHANK YOU FOR USE MY PROGRAM...");
    return 0;
}
