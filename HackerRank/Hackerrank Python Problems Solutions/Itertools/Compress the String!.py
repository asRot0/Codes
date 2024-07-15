from itertools import groupby
print(*[(len(list(x)), int(c)) for c, x in groupby(input())])
