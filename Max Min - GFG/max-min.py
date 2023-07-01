class Solution:
    def findSum(self,A,N): 
        
        if n%2 == 0:
            maxm = max(A[0], A[1])
            minm = min(A[0], A[1])
            i=2
        else:
            maxm = A[0]
            minm = A[0]
            i = 1
        while(i<N-1):
            if A[i] <A[i+1]:
                maxm = max(A[i+1], maxm)
                minm = min(A[i], minm)
            else:
                maxm = max(A[i], maxm)
                minm = min(A[i+1], minm)
            i+= 2
        return maxm+minm



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends