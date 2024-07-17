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

        hex_num[i]=h;
        n/=16;
        i++;
    }
    for(int j=i-1;j>=0;j--){
                    if(h>9){
                        h=i;
            switch(h){
            case 10 : printf("A"); break;
            case 11 : printf("B"); break;
            case 12 : printf("C"); break;
            case 13 : printf("D"); break;
            case 14 : printf("E"); break;
            case 15 : printf("F"); break;
            }
                    }
            else
                    printf("%c",hex_num[j]);
    }
    getch();
    return 0;
}
