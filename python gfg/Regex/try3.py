import re

string = 'britts_54'
pattern = re.compile('[A-Za-z0-9-_]+')
if pattern.fullmatch(string) is not None:
    print('Found ' + string)
else:
    print('Not Found ' + string)

print('-------------------')

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

regex = '\d+'
match = re.findall(regex, string)
print(match)

pattern = re.compile('[0-9]+')
p = pattern.findall(string)
if p is not None:
    print('Found', p)
else:
    print('Not found')
p = re.findall(pattern, string)
print(p) if p is not None else print('no matches found')
