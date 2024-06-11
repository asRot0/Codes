#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;
    for(i=0;i<10;i++)
        printf("%10d %10e %10c %10x %10s\n",rand(), rand(), rand(),rand(),rand());
    return 0;
}
