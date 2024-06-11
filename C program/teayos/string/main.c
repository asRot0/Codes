#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color F1");
    char str[80];
    int i;
    printf("enter a string (less  then 80 chars):");
    gets(str);
    for(i=0;str[i];i++) printf("%c",str[i]);
    return 0;
}
