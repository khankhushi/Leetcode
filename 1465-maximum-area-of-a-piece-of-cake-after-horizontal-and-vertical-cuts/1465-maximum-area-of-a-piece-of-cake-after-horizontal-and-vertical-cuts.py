class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        max_h = 0
        max_v = 0
        for i in range(0, len(horizontalCuts)):
            diff = horizontalCuts[i] - horizontalCuts[i-1]
            max_h = max(max_h, diff)
        for i in range(0, len(verticalCuts)):
            diff = verticalCuts[i] - verticalCuts[i-1]
            max_v = max(max_v, diff)
        return (max_h*max_v % 1000000007)
            
            
        