#include <stdio.h>
#include<conio.h>
#include<string.h>
#include <stdlib.h>
int main()
{
    system("color F1");
    char str[ ]="COMPUTER";
    int i,j,l;
    l=strlen(str);
    for(i=0;i<l;i++){
        for(j=0;j<=i;j++){
            printf("%c",str[j]);
        }
        printf("\n");
    }
    getch();
    return 0;
}
