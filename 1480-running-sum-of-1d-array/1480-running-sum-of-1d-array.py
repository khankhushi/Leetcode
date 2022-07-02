class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        runningSums = 0
        for i in range(len(nums)):
            runningSums += nums[i] 
            runningSum.append(runningSums)
            i+=i
        return runningSum