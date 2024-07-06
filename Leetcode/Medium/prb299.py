class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1 = dict()
        d2 = dict()
        bulls = cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                d1[secret[i]] = d1.get(secret[i], 0) + 1
                d2[guess[i]] = d2.get(guess[i], 0) + 1

        for key in d1:
            if key in d2:
                cows += min(d1[key], d2[key])

        return f'{bulls}A{cows}B'