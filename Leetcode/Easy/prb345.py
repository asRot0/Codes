class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            if left >= right: break
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)


'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in v and s[right] in v:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in v:
                left += 1
            elif s[right] not in v:
                right -= 1
        return ''.join(s)
'''

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vindex = []
        vowels = []
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        s = list(s)
        for i, c in enumerate(s):
            if c not in vowel_set:
                continue
            
            vindex.append(i)
            vowels.append(c)

        l = len(vowels)
        for i, index in enumerate(vindex):
            s[index] = vowels[l-i-1] 
            
        return ''.join(s)
'''

'''
def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1
        s = s[:left] + s[right] + s[left+1:right] + s[right+1:]
        left += 1
        right -= 1
    return s
'''

'''
def reverse_vowels(s):
    vowels = set("aeiouAEIOU")  # Set for efficient vowel checks
    vowel_indices = [(i, char) for i, char in enumerate(s) if char in vowels]

    for i in zip(reversed(vowel_indices), vowel_indices):
        print(i[0][0], i[-1][-1])
        s = s[:i[0][0]] + i[-1][-1] + s[i[0][0] + 1:]
    return s
print(reverse_vowels('leetcode'))
'''