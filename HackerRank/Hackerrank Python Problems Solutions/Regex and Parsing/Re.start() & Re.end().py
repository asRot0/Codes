# def find_substring_indices(string, substring):
#     pattern = r'(?={})'.format(substring)  # Lookahead assertion to find overlapping matches
#     matches = re.finditer(pattern, string)
#     indices = map(lambda match: (match.start(), match.start() + len(substring) - 1), matches)
#     return indices or [(-1, -1)]
#
# string = input().strip()
# substring = input().strip()
#
# indices = find_substring_indices(string, substring)
# for index in indices:
#     print(index)


import re

string, substring = input().strip(), input().strip()

pattern = r'(?={})'.format(substring)
matches = list(re.finditer(pattern, string))

if matches:
    print('\n'.join(str((match.start(), match.start()+len(substring)-1)) for match in matches))
else:
    print(str((-1,-1)))