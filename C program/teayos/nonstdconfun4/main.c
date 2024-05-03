#include <stdio.h>
#include <conio.h>

int main(void)
{
    do{
        printf("%c", '.');
    }while(!kbhit());
    return 0;
}
