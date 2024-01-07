import string

st = 'ABCD'
st1 = 'abdE'

print(''.join(filter(lambda x: x in string.ascii_uppercase, st)) == st)
print(''.join(filter(lambda x: x in string.ascii_lowercase, st1)) == st1)
print(list(map(lambda x: x in string.ascii_lowercase, st1)))
print(all(map(lambda x: x in string.ascii_lowercase, st1)))