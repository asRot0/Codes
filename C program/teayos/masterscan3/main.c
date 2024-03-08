#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int a,b;
    char op;
    printf("enter 1st number, operator, 2nd number :");
    printf("operation ('+,-,*,/')\n");
    scanf("%d %c%d",&a,&op,&b);  //here  is a space in the control string, scanf() will match and discard whitespace characters until the first non-whitespace characters is found
    switch(op){
    case '+' : printf("%d",a+b);
     break;
    case '-' : printf("%d",a-b);
     break;
    case '*' : printf("%d",a*b);
     break;
    case '/' : if(b!=0) printf("%d",a/b);
      }
    return 0;
}
