from collections import namedtuple
N, students = int(input()), namedtuple('students', input())
print(sum([int(students(*input().split()).MARKS) for i in range(N)])/N)
