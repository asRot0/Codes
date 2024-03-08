#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char str[80];
    printf("enter letters, anything else to stop\n");
    scanf("%[a-zA-Z]",str);
    printf(str);
    return 0;
}
