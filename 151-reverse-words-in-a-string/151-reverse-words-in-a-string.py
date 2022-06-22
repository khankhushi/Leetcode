class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_string = " ".join(s.split()[::-1])
        return reverse_string
        