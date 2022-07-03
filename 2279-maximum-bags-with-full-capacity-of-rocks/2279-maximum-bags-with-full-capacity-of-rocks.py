class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:   
        count = 0
        diff = []
        for i in range(len(capacity)):
                diff.append(capacity[i] - rocks[i])
        diff.sort()
        
        for i in range(len(diff)):
                if additionalRocks>= diff[i]:
                    additionalRocks += -diff[i]
                    count += 1 
        return count
                    
                        