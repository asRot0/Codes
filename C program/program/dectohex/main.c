#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int number;
    printf("Decimal number:");
    scanf("%d",&number);
    printf("Hex number=%x",number);
    getch();
    return 0;
}
