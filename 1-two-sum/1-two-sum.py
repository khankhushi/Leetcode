class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return nums.index(target-n), i
            else:
                d[n] = i
        return nums.index(target-n), i
            
         
            
                