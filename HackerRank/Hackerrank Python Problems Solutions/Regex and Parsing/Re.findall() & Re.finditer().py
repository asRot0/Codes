import re

vowels = 'AEIOUaeiou'
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'

pattern = r'(?<=[{0}])([{1}]{{2,}})(?=[{0}])'.format(consonants, vowels)
string = input().strip()

matches = re.findall(pattern, string)
print('\n'.join(matches) if matches else '-1')
