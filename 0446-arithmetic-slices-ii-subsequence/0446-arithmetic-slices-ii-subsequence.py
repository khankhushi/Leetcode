class Solution:
    def numberOfArithmeticSlices(self, A):
        total, n = 0, len(A)
        dp = [Counter() for item in A]
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
        return total
    

            
        