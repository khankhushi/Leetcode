class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1 if num % 2 == 0 or num == 1 else 2
            num //= 2
        return count
        