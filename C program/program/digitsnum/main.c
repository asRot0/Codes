#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int num,digits=0;
    printf("inter your number:");
    scanf("%d",&num);
    do{
        num/=10;
        digits++;
    }while(num>0);
    printf("The number has %d digit(s).",digits);
    getch();
    return 0;
}
