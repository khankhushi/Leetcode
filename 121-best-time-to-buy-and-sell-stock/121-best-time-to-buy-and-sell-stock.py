class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0,1,0
        
        while right < len(prices):
            profit = prices[right]- prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, profit)
            else:
                left = right # next minimum low
            right= right +1
        return max_profit
                