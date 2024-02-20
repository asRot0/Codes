#include <stdio.h>
#include<stdlib.h>
int main()
{
    system("color 37");
    int i,j;
    for(i=1;i<5;i++){
        for(j=1;j<=5;j++){
                if((i==1&&j==1)||(i==2&&j==2)||(i==2&&j==3)||(i==1&&j==2)||(i==2&&j==1))
                            printf(" ");
                    else if(i==1&&j==3)
                            printf("7");
                         else if(i==2&&j==4)
                                 printf("4");
                              else if(i==4&&j==1)
                                      printf("3");
                                    else if(i==3)
                                            printf("_");
                 else
                 printf("X");
        }
        printf("\n");
    }
    getch();
    return 0;
}
