class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.remove(0)
        #         nums.append(0)
                
        nonZeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroCount] = nums[i]
                nonZeroCount += 1
        for i in range(nonZeroCount, len(nums)):
            nums[i] = 0
        return nums
            
            
            