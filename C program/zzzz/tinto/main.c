#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("color 37");
    int n, i=0;
    char bin_num[i];
    scanf("%d",&n);
    while(n>0){
        bin_num[i]=n%16;

         if(i==10){
            i="A";

        }
          if(i==11){
            i="B";

        }
         if(i==12){
            i="C";

        }
         if(i==13){
            i="D";

        }
         if(i==14){

            i="E";

        }
         if(i==15){
            i="F";

        }

        n/=16;
        i++;
    }
    for(int j=i-1;j>=0;j--)
    printf("%d",bin_num[j]);
    getch();
    return 0;
}
