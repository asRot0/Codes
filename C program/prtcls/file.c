#include<stdio.h>
int main()
{
FILE *f1;
char ch;
f1=fopen("input.txt","w");
while((ch=getchar())!='\n')
{
putc(ch,f1);
}
fclose(f1);
f1=fopen("input.txt","r");
while((ch=getc(f1))!=EOF)
{
printf("%c",ch);
}
fclose(f1);

}
