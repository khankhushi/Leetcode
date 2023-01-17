class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        ones = 0
        for num in s:
            if num =='1':
                ones += 1
            else:
                res += 1
                if res > ones:
                    res = ones                    
        return res