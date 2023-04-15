class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n=len(piles)
        topk=[]
            
        cur_arr=[0]*(k+1)
        max_arr=[0]*(k+1)
        
        for x in piles:
            i=0
            cursum=0
            while i<k and i<len(x):
                cursum+=x[i]
                j=0
                while i+1+j<=k:
                    if j>0 and max_arr[j]==0:
                        break
                    cur_arr[i+1+j]=max(cur_arr[i+1+j],max_arr[j]+cursum)
                    j+=1
                i+=1
                
            for t in range(i+j):
                if cur_arr[t]>max_arr[t]:
                    max_arr[t]=cur_arr[t]
                    
        return max_arr[k]