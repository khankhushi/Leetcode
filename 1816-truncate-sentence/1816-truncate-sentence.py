class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = list(s.split(" "))
        string = " "
        return string.join(li[:k])
         