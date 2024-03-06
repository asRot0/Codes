age = int(input())
t = [365, 30, 1]
ans = []
text = ['ano(s)', 'mes(es)', 'dia(s)']
for i in t:
    quotient = int(age / i)
    ans.append(quotient)
    remainder = age % i
    age = remainder
for j in range(3):
    print(ans[j], text[j])