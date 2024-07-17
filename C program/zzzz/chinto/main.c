#include <stdio.h>
#include <stdlib.h>
int main()
{//dec to hex...
    system("color 37");
    int n, i=0,h;
    int hex_num[i];
    scanf("%d",&n);
    while(n>0){
            h=n%16;
            if(h>9)
            switch(h){
            case 10 : h='A'; break;
            case 11 : h='B'; break;
            case 12 : h='C'; break;
            case 13 : h='D'; break;
            case 14 : h='E'; break;
            case 15 : h='F'; break;
            }
        hex_num[i]=h;
        n/=16;
        i++;
    }
    for(int j=i-1;j>=0;j--)
    printf("%c",hex_num[j]);
    getch();
    return 0;
}
