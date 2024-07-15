import re

s = input()
lowercase = sorted(re.findall('[a-z]', s))
uppercase = sorted(re.findall('[A-Z]', s))
odd_number = sorted(x for x in re.findall('[0-9]', s) if int(x) % 2 != 0)
even_number = sorted(x for x in re.findall('[0-9]', s) if int(x) % 2 == 0)

print(''.join(lowercase + uppercase + odd_number + even_number))
