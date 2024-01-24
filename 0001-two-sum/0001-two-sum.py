class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]== target and i!=j:
        #             res.append(i)
        #             res.append(j)
        #         else:
        #             continue
        # return res
        
        
        # idx = 0
        # for i in range(len(nums)):
        #     complement = target-nums[i]
        #     if complement in nums:
        #         idx = nums.index(complement)
        #     ## condition that same element can't be used twice:
        #     if idx == i:
        #         continue
        #     break
        # return idx,i
        
        
        # using dictionary
        stre = dict()
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in stre:
                return [stre[comp], i]
            else:
                stre[nums[i]] = i