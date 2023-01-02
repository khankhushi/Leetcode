class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        cou = 0
        for sent in range(len(s)):
            s[sent] = s[sent].count(" ")+1
            cou = max(cou, s[sent])
        return cou
