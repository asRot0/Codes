#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(void)
{
    char str[20];
    int a;

    printf("enter your car:");
    gets(str);
    {


    if(!strcmp(str, "cycle")){
        printf("cross");
        goto pos1;
    }
    printf("enter position:");
    scanf("%d",&a);
    if(a<5)
        printf("can't cross");
    else
        printf("cross");

    }
    pos1:
    printf("\nyour vehicle ");
    printf(str);
    return 0;
}
