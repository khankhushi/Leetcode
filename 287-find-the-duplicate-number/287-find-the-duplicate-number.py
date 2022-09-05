class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        
        while (left<=right):
            mid = (left+right)//2
            count = 0

            for n in nums:
                if n<=mid:
                    count+=1
            if count>mid:
                repeat = mid
                right = mid-1 
            else:
                left= mid+1
        return repeat
            
        
        
        
        
        
        
        
        
        # Uses extra space
        
        # repeat = set()
        # for n in nums:
        #     if n in repeat:
        #         return n
        #     else:
        #         repeat.add(n)
        
        
        
        #TLE
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]== nums[j]:
        #             return nums[j]
        