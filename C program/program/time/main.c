#include <stdio.h>
#include <time.h>

int main(void)
{
    time_t lt;
    lt = time(NULL);
    printf(ctime(&lt));
    return 0;
}
