class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            # for j in range (0,len(nums)):
            for j in range (i+1,len(nums)): # Since we have already traversed till i and are finding a pair ahead
                if target == nums[j] + nums[i]:
                    return i, j