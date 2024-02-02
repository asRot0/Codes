#include<stdio.h>
main()
{
int x,i=0,a[20],j;
printf("Enter the Integer number : ");
scanf("%d",&x);
while(x!=0)
{
a[i]=x%2;
x=x/2;
i++;
}
printf("The Binary Number : ");
for(j=i-1;j>=0;j--)
printf("%d",a[j]);
getch();
}
