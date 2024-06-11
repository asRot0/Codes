#include <stdio.h>
#include <stdlib.h>
#include<conio.h>
enum transport {car, train, airplane, bus} tp ;
char trans[ ][20]={
    "car", "train", "airplane", "bus"
};
int main(void)
{
    printf("press a key to select transport:");
    while(!kbhit()) rand();
    getch();
    tp = rand() % 4;
    printf("%s", trans[tp]);
    return 0;
}
