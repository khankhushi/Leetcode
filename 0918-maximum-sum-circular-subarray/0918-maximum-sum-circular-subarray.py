class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, max_so_far, max_ending_here, min_so_far, min_ending_here = sum(nums), nums[0], nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_so_far, min_so_far = max(max_so_far + nums[i], nums[i]), min(min_so_far + nums[i], nums[i])
            max_ending_here, min_ending_here = max(max_ending_here, max_so_far), min(min_ending_here, min_so_far)
        return max_ending_here if min_ending_here == total else max(max_ending_here, total - min_ending_here)