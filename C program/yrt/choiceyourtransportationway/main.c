#include <stdio.h>
#include <stdlib.h>
int main()
{
    int tk,saved_tk,i=0;
    printf("How much money do you have...");
    scanf("%d",&tk);
    printf("\n");
        if(tk>=200){
            printf("you can go Uber and");
            i++;
            saved_tk=tk-200;
            printf(" saved your %d tk.",saved_tk);
            printf("\n\n");}
        if(tk>=100){
            printf("you can go Pathao and");
            i++;
            saved_tk=tk-100;
            printf(" saved your %d tk.",saved_tk);
            printf("\n\n");}
        if(tk>=100||tk>20){
            printf("you can get another seating service.");
            i++;
            printf("\n\n");}
        if(tk<20)
            printf("you have less money to travel.\n");
    printf("you can travel %d way(s).\n",i);
    printf("//HAPPY JOURNEY//");
    getch();
    return 0;
}
