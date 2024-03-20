class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)

        for i in range(len(s)):
            while indices[i] != i:
                s[indices[i]], s[i] = s[i], s[indices[i]]
                indices[indices[i]], indices[i] = indices[i], indices[indices[i]]
        return ''.join(s)