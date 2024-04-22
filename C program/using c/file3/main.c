#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp1;
    int a;
    fp1=fopen("numberfile.txt","r");
    while(a=getw(fp1)!=EOF){
        printf("%d\t",a);
    }
    fclose(fp1);
    return 0;
}
