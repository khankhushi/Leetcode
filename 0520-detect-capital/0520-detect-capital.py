class Solution:
    def detectCapitalUse(self, word: str) -> bool:
#       # All CAPS
#         for i in range(len(word)):
#             if word[i].isupper():
#                 match1 = True
#             else:
#                 match1 = False
#         # all lower
#         for i in range(len(word)):
#             if word[i].islower():
#                 match2 = True
#             else:
#                 match2 = False
        
#         # first letter CAPS
#             if word[0].isupper():
#                 match3 = True
#             for i in range(1,len(word)):
#                 if word[i].islower():
#                     match3 = True
#         return False
    
    
        countU,countL = 0,0
        if len(word) == 1:
            return True
        if word[0].isupper():
            countU += 1
        for i in range(1,len(word)):
            if word[i].isupper():
                countU += 1
            elif word[i].islower():
                countL += 1
        if countU == len(word):
            return True
        elif countL+1 == len(word):
            return True
        else:
            return False
       
                
                
                
            
            
            
            