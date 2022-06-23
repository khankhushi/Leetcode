class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = " ".join(list(s.split())[:k])
        return s
        
        