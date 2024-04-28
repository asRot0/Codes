#include <stdio.h>
#include <stdlib.h>
int main()
{system("color F1");
    int choice;
    printf("1:dec to bin\n");
    printf("2:dec to oct\n");
    printf("3:dec to hex\n");
    printf("choice number:");
    scanf("%d",&choice);
    if(choice==1){
        int n, i=0;
    int bin_num[i];
    scanf("%d",&n);
    while(n>0){
        bin_num[i]=n%2;
        n/=2;
        i++;
    }
    for(int j=i-1;j>=0;j--)
    printf("%d",bin_num[j]);
    }
    else if(choice==2){
           int number;
    printf("Decimal number:");
    scanf("%d",&number);
    printf("Oct number=%o",number);
    }
    else{
        int number;
    printf("Decimal number:");
    scanf("%d",&number);
    printf("Hex number=%x",number);
    }
    getch();
    return 0;
}
