import re

for _ in range(int(input())):
    line = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: ['or', 'and'][x.group()=='&&'], line))