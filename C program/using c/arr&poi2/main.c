#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(void)
{
    char *s1="fdhfj",ch[20];
    int len,i;
     len=strlen(s1);
    for(i=0;i<len;i++){
        s1[i]=s1[i];
    }
printf("%s",s1);
return 0;
}
