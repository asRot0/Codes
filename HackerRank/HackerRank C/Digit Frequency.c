int main() {
    int arr[10] = {0};
    char *s;
    s = malloc(1000*sizeof(char));
    scanf("%[^\n]%*c", s);
    for(int i=0; i<strlen(s); i++)
    {
        if(isdigit(*(s+i))) // check if digit
        {
           int a = *(s+i)-'0'; // convert to int
           arr[a]++;
        }
    }
    for(int i=0; i<10; i++)
    {
        printf("%d ",arr[i]);
    }
return 0;
}
