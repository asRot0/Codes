#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int reverse,bin,dec,Bin;
    reverse=0,bin=0;
    printf("Input Decimal number:");
    scanf("%d",&dec);
    while(dec>0){
        bin=(bin*10)+(dec%2);
        dec=dec/2;
    }
    for(Bin=bin-1;Bin>=0;Bin--)
    printf("Binary number=%d",Bin);
    return 0;
}
