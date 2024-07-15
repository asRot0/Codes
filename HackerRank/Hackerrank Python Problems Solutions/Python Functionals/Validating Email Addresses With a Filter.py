'''
import re

def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
 '''

import re

def fun(s):
    # return True if s is a valid email, else return False
    email_part1 = str(s).rsplit('@', 1)
    
    pattern = re.compile('[A-Za-z0-9-_]+')
    pattern1 = re.compile('[A-Za-z0-9]+')
    pattern2 = re.compile('[A-Za-z]+')
    
    if len(email_part1) == 2 and pattern.fullmatch(email_part1[0]) is not None:
        email_part2 = email_part1[1].rsplit('.', 1)
        if len(email_part2) == 2 and pattern1.fullmatch(email_part2[0]) is not None:
            if len(email_part2[1]) < 4 and pattern2.fullmatch(email_part2[1]) is not None:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
