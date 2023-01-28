class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        def sentencelen(string: str):
            cnt = 0
            for i in string:
                if i== " ":
                    cnt+= 1
            return cnt+1
        maximum = 0
        for i in sentences:
            maximum = max(sentencelen(i), maximum)
        return maximum
        