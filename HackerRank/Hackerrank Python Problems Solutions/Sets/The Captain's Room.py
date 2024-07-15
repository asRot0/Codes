k, room = int(input().strip()), list(map(int, input().strip().split()))
room_no = set(room)
print((sum(room_no)*k - sum(room))//(k-1))


'''
from collections import Counter

k = int(input())
roomNum = list(map(int,input().split()))

roomNumCounter = Counter(roomNum)
#print(min(roomNumCounter, key=roomNumCounter.get))
print(roomNumCounter.most_common()[-1][0])
'''
