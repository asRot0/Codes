#include <stdio.h>

int main(void)
{
    int i;
    do{
        i=getchar();
        if(i==EOF){
            printf("error on input");
            break;
        }
        if(putchar('.')==EOF){
            printf("error on output");
            break;
        }
    }while((char) i!='\n');
    return 0;
}
