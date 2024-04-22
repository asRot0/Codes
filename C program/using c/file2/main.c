#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <ctype.h>
void main()
{
    FILE *fptr;
    char ch='y',name[20];
    int age;
    float salary;
    if((fptr=fopen("EMP.txt","w"))==NULL){
        printf("unable to open a file.");
        exit(0);
    }
    while(ch=='y'){
        printf("\nenter name:");
        gets(name);
        printf("\nenter age:");
        scanf("%d",&age);
        printf("\nenter salary:");
        scanf("%f",&salary);
        fprintf(fptr,"%s %d%f",name,age,salary);
        fflush(stdin);
        printf("\nany more input(y/n):");
        ch=tolower(getche());
    }
    fclose(fptr);
}
