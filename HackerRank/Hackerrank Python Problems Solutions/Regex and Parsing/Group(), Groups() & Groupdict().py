import re

match = re.search(r'([\w](?!_))\1+', input().strip())
print(match.group(1) if match else -1)