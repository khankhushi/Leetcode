class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeat = set()
        for n in nums:
            if n in repeat:
                return n
            else:
                repeat.add(n)
        
        
        
        
        
        
        #TLE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]== nums[j]:
        #             return nums[j]
        