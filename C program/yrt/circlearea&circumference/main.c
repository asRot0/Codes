#include <stdio.h>
int main()
{
    int r;
    float area, circumference, dif;
    printf("Enter the value of r:");
    scanf("%d",&r);
    area=3.1416*r*r;
    circumference=2*3.1416*r;
    printf("Area Is= %.2f", area);
    printf("\ncircumference Is= %.2f", circumference);
    printf("\n       Now,If you want Differerce.\nEnter the values of Area & circumference:");
    scanf("%f%f",&area,&circumference);
    dif=area-circumference;
    printf("Difference Is= %f", dif);
    return 0;
}
