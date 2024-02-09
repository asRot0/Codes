#include <stdio.h>
#include<conio.h>
#include<string.h>
#include <stdlib.h>
int main()
{//slow string..............
    system("color 8F");
    char str[ ]="we are students";
    int i,j,p,l;
    l=strlen(str);
    for(i=0;i<l;i++){
     if(i==6)
        continue;
        for(j=0;j<=i;j++)
            {
                for(p=1;p<=129999999;p++){
                    if(p==129999999){
                        printf("%c",str[j]);
                    }
                }
        }
        printf("\n");
    }
    getch();
    return 0;
}
