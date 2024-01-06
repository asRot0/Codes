'''
    MetaCharacters
    To understand the RE analogy, MetaCharacters are useful, important, and
    will be used in functions of module re. Below is the list of metacharacters.

    MetaCharacters	Description

    \	Used to drop the special meaning of character following it
    []	Represent a character class
    ^	Matches the beginning
    $	Matches the end
    .	Matches any character except newline
    |	Means OR (Matches with any of the characters separated by it.
    ?	Matches zero or one occurrence
    *	Any number of occurrences (including 0 occurrences)
    +	One or more occurrences
    {}	Indicate the number of occurrences of a preceding regex to match.
    ()	Enclose a group of Regex
'''

# Let’s discuss each of these metacharacters in detail
import re

# \ – Backslash
print('backslash........')
str1 = '\nfind the dot(.)'
match = re.search(r'.', str1)  # except newline
match2 = re.search(r'\.', str1)
print(match)
print(match2)

# [] – Square Brackets
print('\nsquare brackets....')
string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
pattern2 = '[^a-m]'  # using the caret(^) [^a-c] means any character except a, b, or c
result = re.findall(pattern, string)
result2 = re.findall(pattern2, string)
print(result)
print(result2)

# ^ – Caret
print('\ncaret......')
# Caret (^) symbol matches the beginning of the string
pattern = r'^The'  # Match strings starting with "The"
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
print(strings)
for string in strings:
    if re.match(pattern, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')
print(re.match(pattern, strings[0]))

# $ – Dollar
print('\ndollar......')
# Dollar($) symbol matches the end of the string
string = 'hello world!'
pattern = r'world!$'
print('str:', string, 'and pattern:', pattern)
print('pattern matched') if re.search(pattern, string) else print('pattern not found')

# . – Dot
print('\ndot.......')
# Dot(.) symbol matches only a single character except for the newline character (\n)
string = "The quick brown fox jumps over the lazy dog"
pattern = r"brown.fox"

match = re.search(pattern, string)
print(match)
if match:
    print("Match found!")
    print(match.group())
else:
    print("Match not found.")

print('---------------')
strings = ['Nbr35', 'd-dd', '25342', '43Edh']
pattern = r'[A-Z0-9]+'
print(strings)
for st in strings:
    if re.match(pattern, st):
        # print(re.search(pattern, st))
        print('matched', st)
    else:
        print('not matched', st)
print('-----------------------------')

string = 'britts_54'
pattern = re.compile('[A-Za-z0-9-_]+')
if pattern.fullmatch(string) is not None:
    print('Found ' + string)
else:
    print('Not Found ' + string)
print('---------------------')

strings = ['britts_54', 'BRD-12', 'Tdef*65']
pattern = re.compile('[A-Za-z0-9-_]+')
print(pattern)
for st in strings:
    if pattern.fullmatch(st) is not None:
        print('Found ' + st)
    else:
        print('Not Found ' + st)
print('-------------')
