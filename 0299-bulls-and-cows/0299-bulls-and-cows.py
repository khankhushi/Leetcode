class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows, bulls = 0, 0
        cnt = Counter(secret)
        for s,g in zip(secret, guess):
            if s== g:
                bulls += 1
                if cnt[s]:
                    cnt[s] -= 1
                else:
                    cows -= 1
            elif cnt[g]:
                cows += 1
                cnt[g] -= 1
                    
        return (str(bulls)+"A"+ str(cows)+"B")