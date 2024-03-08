#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *p,str[80];
    printf("enter a string:");
    p=gets(str);
    if(p) // if not null
        printf("%s %s\n",p,str);
    if(gets(str))
            puts(str);
    return 0;
}
