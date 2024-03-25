#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *f1,*f2;
    char c;
    f1=fopen("textfile.txt","a");
    while((c=getchar())!='\n'){
        putc(c,f1);
    }
    fclose(f1);
    f1=fopen("textfile.txt","r");
    f2=fopen("outputfile.txt","a");
    while((c=getc(f1))!=EOF){
        putc(c,f2);
    }
    fclose(f1);
    fclose(f2);
    getch();
}
