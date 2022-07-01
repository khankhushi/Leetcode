class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sorting the boxes with highest number of boxes
        boxTypes.sort(key= lambda x: x[1], reverse=True) # /  boxTypes.sort(key= lambda x: -x[1])
        total_units = 0
        for numBoxes, units in boxTypes:
            #edge case where truckSize <= numBoxes
            if truckSize <= 0:
                return total_units
            total_units += (min(numBoxes, truckSize))*units
            truckSize -= numBoxes
        
        return total_units
        
                    
                    
        