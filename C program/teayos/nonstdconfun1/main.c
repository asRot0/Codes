#include <stdio.h>
#include <conio.h>
#include <ctype.h>

int main(void)
{
    char ch;
    do{
        ch=getch();
         if (ch!='q'&&ch!='Q')
        printf("%c",toupper(ch));
    }while(ch!='q'&&ch!='Q');
    return 0;
}
