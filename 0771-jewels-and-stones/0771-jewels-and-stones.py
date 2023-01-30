class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        setJewels = set(jewels)
        return sum(s in setJewels for s in stones)