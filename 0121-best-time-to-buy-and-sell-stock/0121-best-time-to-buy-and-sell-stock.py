class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minimum = prices[0]
        for i in range(len(prices)):
            profit = prices[i]-minimum
            maxP = max(maxP, profit)
            minimum = min(minimum, prices[i])
        return maxP
        

        