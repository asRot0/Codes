#include<stdio.h>
main()
{
int a[30],i,num,largest,smallest;
printf("\nEnter no of elements: ");
scanf("%d", &num);
for(i=0;i<num;i++)
scanf("%d",&a[i]);
largest=a[0];
smallest=a[0];
for(i=1;i<num;i++)
{
if(a[i]>largest)
{
largest=a[i];
}
if(a[i]<smallest)
{
 smallest=a[i];
}
}
printf("\nLargest Element : %d",largest);
printf("\nSmallest Element : %d",smallest);
getch();
}
