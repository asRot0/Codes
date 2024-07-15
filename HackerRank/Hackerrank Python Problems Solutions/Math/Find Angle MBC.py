import math

ab, bc = int(input()), int(input())
angle = math.atan2(ab, bc)
print(round(math.degrees(angle)), end=chr(176))
