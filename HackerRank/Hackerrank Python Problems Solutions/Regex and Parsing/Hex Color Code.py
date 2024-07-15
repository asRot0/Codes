import re

for _ in range(int(input())):
    matches = re.findall(r'(?<!^)(#(?:[\da-f]{3}){1,2})', input(), re.I)
    if matches:
        print(*matches, sep='\n')