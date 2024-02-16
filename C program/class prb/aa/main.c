#include<stdio.h>
int main()
{
int X,s=1;
scanf("%d",&X);
printf("\n");
do
{
    if(s%2!=0)
        printf("%d\n",s);
        s=s+1;
}
while(s<=X&&X<=1000);
return 0;

}
