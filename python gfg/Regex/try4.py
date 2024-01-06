import re

string = 'a dog bitten by a snake is afraid of sausages'
pattern = re.compile('[a-z]')

print(pattern.findall(string))
print(pattern.fullmatch(string))


# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he \
said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W+')
print(p.findall("he said *** in some_language."))

p = re.findall('\d+', "233 23 he 4 5said *** in some_language.")
print(p)
