import re

for _ in range(int(input())):
    name, email_address = re.findall(r'^([^<]+)<([^>]+)>$', input().strip())[0]

    if re.match(r'^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_address):
        print("{} <{}>".format(name.strip(), email_address))
