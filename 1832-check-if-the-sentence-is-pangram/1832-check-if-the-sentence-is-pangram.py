class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # for i in sentence:
        #     if ord(i) in range(ord(chr(97)), ord(chr(123)):
        #              return True
        cnt = 0
        st = set(sentence)
        for i in st:
            if ord(i) in range(97,123):
                cnt += 1
                
        if cnt == 26:
            return True
        else:
            return False