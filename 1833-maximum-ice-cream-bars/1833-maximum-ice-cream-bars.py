class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for i in range(len(costs)):
            if costs[i] <= coins:
                cnt+= 1
                coins -= costs[i]
            else:
                break
        return cnt
                
        