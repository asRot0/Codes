#include <stdio.h>
#include <stdlib.h>
#include<conio.h>
enum transport {car, train, airplane, bus} tp ;
int main(void)
{
    printf("press a key to select transport:");
    while(!kbhit()) rand();
    getch();
    tp = rand() % 4;
    switch(tp){
        case car : printf("car");
        break;
        case train : printf("train");
        break;
        case airplane : printf("airplane");
        break;
        case bus : printf("bus");
    }
    return 0;
}
