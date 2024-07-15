_, sub = map(int, input().split())
li_sub = [map(float, input().split()) for _ in range(sub)]
for mr_sub in zip(*li_sub):
    print(sum(mr_sub)/sub)
