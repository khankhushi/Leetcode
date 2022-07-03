class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        p, n = 1,1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                n = p + 1
            elif nums[i]>nums[i-1]:
                p = n + 1
        return max(p, n)