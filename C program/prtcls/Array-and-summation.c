#include<stdio.h>
main()
{
int i,arr[10],sum=0
,num;
printf("\n How many elements: ");
scanf("%d",&num);
printf("\nEnter the values: ");
for(i=0;i<num;i++)
{
scanf("%d",&arr[i]);
sum=sum+arr[i];
}
for(i=0;i<num;i++)
printf("\n%d",arr[i]);
printf("\nsum=%d",sum);
}
