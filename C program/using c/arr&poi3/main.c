#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
int main(void)
{
    char *s,ch;
    int c=0,v=0;
    printf("enter a line of text:");
    gets(s);
    printf("\n");
    while(*s){
        ch=toupper(*s);
        if(ch>='A'&&ch<='Z'){
            switch(ch)
            {
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                v=v+1;
                printf("%c",ch);
                break;
            default:
                c=c+1;
                printf("%c",ch);
                break;
            }
        }
        ++s;
    }
    printf("\n\nvowel=%d\nconsonant=%d",v,c);
    getch();
    return 0;
}
