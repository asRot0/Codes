#include <stdio.h>
#include <ctype.h>

int sum_array(const int a[ ], int n)
{
    int i,sum;
    sum=0;
    for(i=0;i<n;i++)
        sum+=a[i];
    return sum;
}
int main(void)
{
    char *a[15], x;
    int y,add;
    add= sum_array(15,3);
    printf("%d",add);
    return 0;
}
