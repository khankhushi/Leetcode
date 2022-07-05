class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        count= 0
        max_length = min(1, len(nums))
        nums.sort()
        for i in range(len(nums)):
                if nums[i] - nums[i-1] == 1:
                    count += 1
                    max_length = max(max_length, count)
                elif nums[i] == nums[i-1]:
                    continue
                else:
                    count = 1
        return max_length
                    