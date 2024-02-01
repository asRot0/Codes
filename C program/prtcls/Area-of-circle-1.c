#include<stdio.h>
#define pi 3.1416
//By "#define pi 3.1416" we have considered pi as a constant. So, we don't have to mention "pi=3.1416" in the main function section.
main()
{
float r,area;
//we use "float" in terms of floating point.but when we use integer as variables then we use "int". In this program if we want to use radius(r) as an integer and area as a floating point then the code will be "int r;float area;"
printf("RADIUS: ");
//Here "printf" function is used for displaying "RADIUS" on the monitor.
scanf("%f",&r);
//In this phase "%f" means floating point. But we must use "%d" for integer.NB: we must use "&" before the variables in scanf function.
area=pi*r*r;
//In this phase we have calculated the area of a circle.
printf("AREA=\n%f",area);
//Here we have used "\n" to show the result in the next line.NB:we will never use "&" before the variables in printf function.
}
