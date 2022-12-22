class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#         Runningsum = []
#         Rsum = 0
#         for i in range(len(nums)):
#             Rsum += nums[i]
#             Runningsum.append(Rsum)
            
#         return Runningsum
            
        res = [nums[0]]
        for num in nums[1::]:
            res.append(res[-1] + num)
        return res