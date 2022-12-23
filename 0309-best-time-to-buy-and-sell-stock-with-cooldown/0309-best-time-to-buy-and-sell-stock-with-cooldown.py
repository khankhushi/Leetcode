class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, sell, hold = 0, 0, -float('inf')
        
        for stock_pr_odI in prices:
            
            prev_cooldown, prev_sell, prev_hold = cooldown, sell, hold
            
            cooldown = max(prev_cooldown, prev_sell)
            sell = prev_hold + stock_pr_odI
         
            hold = max(prev_hold, prev_cooldown - stock_pr_odI)
        
        return max(sell, cooldown)