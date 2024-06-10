class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = [c for c in s if c in vowels]
        l.sort(reverse=True)
        return ''.join(l.pop() if c in vowels else c for c in s)