#include <stdio.h>
void bubble_sort(int list[], int n);

int main() {
  int n;
  scanf("%d",&n);
  if (n<3){
    printf("n is not greater than 2");
    return 0;
  }
  int arr[n][n];
  for(int i=0;i<n;i++){
    for (int j=0;j<n;j++){
      scanf("%d",&arr[i][j]);
    }
  }

  // QA
  int copyArr[2][n];
  for(int i=0;i<2;i++){
    for (int j=0;j<n;j++){
      copyArr[i][j] = arr[i][j];
    }
  }

  printf("Matrix Copied :\n");
  for(int i=0;i<2;i++){
    for (int j=0;j<n;j++){
      printf("%d",copyArr[i][j]);
    }
    printf("\n");
  }

  // QB
  printf("Matrix Sorted :\n");
  for(int i=0;i<2;i++){
    int tmp[n];
    for (int j=0;j<n;j++){
      tmp[j] = copyArr[i][j];
    }
    bubble_sort(tmp,n);
    for (int j=0;j<n;j++){
      copyArr[i][j] = tmp[j];
      printf("%d",copyArr[i][j]);
    }
    printf("\n");
  }
  return 0;
}

void bubble_sort(int list[], int n)
{
  int c, d, t;
  for (c = 0 ; c < n - 1; c++) {
    for (d = 0 ; d < n - c - 1; d++) {
      if (list[d] > list[d+1]) {
        t         = list[d];
        list[d]   = list[d+1];
        list[d+1] = t;
      }
    }
  }
}
