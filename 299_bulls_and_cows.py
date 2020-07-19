'''
leetcode: 299
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bulls += 1
        d1 = dict(collections.Counter(list(secret)))
        d2 = dict(collections.Counter(list(guess)))
        for j in d1:
            if j in d2:
                cows += min(d1[j],d2[j])
        cows -= bulls
        return str(bulls)+"A"+str(cows)+"B"

