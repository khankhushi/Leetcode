#User function Template for python3
from collections import defaultdict
class Solution:
    def gcd(self,a,b):
        if (b==0):
            return a
        return self.gcd(b,a%b)
    def countFractions(self, n, numerator, denominator):
        # Your code here
        s=defaultdict(int)
        ans=0
        for i in range(n):
            d=self.gcd(numerator[i],denominator[i])
            numerator[i]/=d
            denominator[i]/=d
            x=numerator[i]
            y=denominator[i]
            w=y-x
            f=y
            if (w,f) in s:
                ans+=s[(w,f)]
            s[(x,y)]+=1
        return ans
                    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends