class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            ans = candies[i] + extraCandies
            if max(candies) > ans:
                result.append(False)
            else:
                result.append(True)
        return result
                
        