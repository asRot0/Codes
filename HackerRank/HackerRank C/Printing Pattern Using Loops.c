#include <stdio.h>

int main()
{
    int n, i, j, size;
    scanf("%d", &n);
    size = n * 2 - 1;

    for (i = 0; i < size; i++) {
        int n_copy, deepth;
        n_copy = n;
        deepth = (i < ((size / 2) + 1)) ? i : size - (i+1);
        for (j = 0; j < size; j++) {
            if (j < deepth)
                printf("%d ", n_copy--);
            else if (j >= size - deepth)
                printf("%d ", ++n_copy);
             else if (j >= deepth && j < size - deepth)
                printf("%d ", n_copy);
        }
        printf("\n");
    }

    return 0;
}
