#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
double get_area(triangle t) {
    double p = (t.a + t.b + t.c) / 2.0;
    double s = sqrt(p * (p-t.a) * (p-t.b) * (p-t.c));
    return s;
}

int compare(const void *tr1, const void *tr2) {
    triangle *t1 = (triangle*)tr1;
    triangle *t2 = (triangle*)tr2;
    if (get_area(*t1) < get_area(*t2))
        return -1;
    return 1;
}

void sort_by_area(triangle *tr, int n) {
    qsort(tr, n, sizeof(triangle), compare);
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}