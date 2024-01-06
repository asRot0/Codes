import itertools
import re

str1 = 'happy coding! nothing to say.. '
# Here r character (r’portal’) stands for raw, not regex

match = re.search(r'say\.\. ', str1)
print(match)
print(match.group(), match.span())
print(match.start(), match.end())

print(''.join(itertools.islice(str1, match.start(), match.end())))
print(str1[slice(match.start(), match.end())])
print(slice(match.start(), match.end()))
print(str1[match.start():match.end()]+'|')
print(len(str1[match.start():match.end()]))
