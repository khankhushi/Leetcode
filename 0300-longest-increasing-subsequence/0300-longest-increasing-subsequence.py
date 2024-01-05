class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for number in range(n):
            for i in range(number):
                if nums[number] > nums[i]:
                    dp[number] = max(dp[number], dp[i]+1)
        return max(dp)
        