#include <stdio.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    short n             = 0;
    short *pn           = &n;
    short *pa           = NULL;
    unsigned int val    = 0;

    if(scanf("%hd", pn) != 1)
    {
        printf("scanf error.");
        exit(EXIT_FAILURE);
    }
    fflush(stdin);

    pa = malloc(n*sizeof(short));

    for(short i=0; i<n; i++)
    {
        scanf("%hd", (pa+i));
        val = val + *(pa+i);
    }
    fflush(stdin);
    printf("%d", val);

    free(pa);

    return 0;
}
