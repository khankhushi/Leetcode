class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Runningsum = []
        Rsum = 0
        for i in range(len(nums)):
            Rsum += nums[i]
            Runningsum.append(Rsum)
            
        return Runningsum
            