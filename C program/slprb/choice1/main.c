#include <stdio.h>
int main()
{
    float num;
    int choice;
    printf("1:Feet to Meters, 2:Meters to Feet.\n");
    printf("Enter choice:");
    scanf("%d",&choice);
    if(choice==1)
    {
        printf("Enter number of feet:");
        scanf("%f",&num);
        printf("Meters:%.3f\n",num/3.28);
    }
    else
    {
        printf("Enter number of meters:");
        scanf("%f",&num);
        printf("Feet:%.3f\n",num*3.28);
    }
    return 0;
}
