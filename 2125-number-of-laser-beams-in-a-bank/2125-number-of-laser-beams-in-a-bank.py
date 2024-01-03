class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans, prev = 0, 0
        for string in bank:
            cnt1 = string.count('1')
            if cnt1 == 0: continue
            ans += prev * cnt1
            prev = cnt1
            
        return ans
        