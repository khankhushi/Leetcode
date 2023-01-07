class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, start, trip = 0, 0,0
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            trip += gas[i]- cost[i] 
            tank += gas[i]- cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        return start if trip >= 0 else -1






#         maximum = max(cost)
#         index = cost.index(maximum)
#         for i in range(len(gas)):
#             ins = index % len(gas)
#             tank += gas[ins]
#             while tank> 0 and ins != index:
#                 tank -= cost[ins+1]
#                 tank += gas[ins+1]
#                 return index
#                 ins+= 1
#         if tank > 0:
#             return index
#         else:
#             return -1
        
    
            
            
            