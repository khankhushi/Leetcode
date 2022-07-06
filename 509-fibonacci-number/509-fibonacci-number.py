class Solution:
    def fib(self, num: int) -> int:
        n0 = 0
        n1 = 1
        nextTerm = 0
        for i in range(1,num):
            nextTerm = n1 + n0
            n0 = n1
            n1 = nextTerm
            i+=1
        if num<=1:
            return num
        else:
            return nextTerm
            
        
            
        

            
        
            