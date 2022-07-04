class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]* len(ratings)
        
        for r in range(1,len(ratings)):
            if ratings[r] > ratings[r-1]:
                candies[r] = candies[r-1] + 1
        for r in range(len(ratings)-1, 0, -1):
            if ratings[r-1] > ratings[r]:
                candies[r-1] = max(candies[r]+1, candies[r-1])
        return sum(candies)