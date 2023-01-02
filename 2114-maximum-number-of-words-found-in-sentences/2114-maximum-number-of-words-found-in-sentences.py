class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cnt,count = 0,0
        for sent in sentences:
            cnt = 0
            for i in range(len(sent)):
                if sent[i] == " ":
                    cnt +=1
                count = max(count, cnt)
        return count+1