#include <stdio.h>
#include <conio.h>
int func(void);
int main(void)
{
    int num;
    num =func();
    printf("%d",num);
    getch();
    return 0;
}
int func(void)
{
    return 10;
}
