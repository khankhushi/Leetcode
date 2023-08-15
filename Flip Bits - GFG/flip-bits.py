#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        cnt = 0
        for i in range(n):
            if a[i]==1:
                a[i] = -1
                cnt += 1
            else:
                a[i] = 1
            
        sm = 0
        ans = 0
        for j in range(n):
            sm += a[j]
            ans = max(sm,ans)
            
            if sm<0:
                sm = 0
        
        return ans+cnt
    
            
            
        
        # Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends