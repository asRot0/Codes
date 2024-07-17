#include <stdio.h>
#include <conio.h>
void main()
{
   "clrscr()";
    int h=0,m=0,s=0;
    printf("Set your time..");
    scanf("%d%d%d",&h,&m,&s);
    start:
        for(h;h<24;h++){
            for(m;m<60;m++){
                for(s;s<60;s++){
                       "clrscr()";
                    printf("%d:%d:%d",h,m,s);

                          }
             s=0;   }
      m=0;     }
        goto start;
   getch();
}
