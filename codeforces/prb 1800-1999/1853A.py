# for s in[*open(0)][2::2]:a=*map(int,s.split()),;print(max(0,min(y-x+2>>1for
# x,y in zip(a,a[1:]))))


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    diff = min((arr[i+1]-arr[i] for i in range(n-1)))
    print(max(0, diff//2+1))