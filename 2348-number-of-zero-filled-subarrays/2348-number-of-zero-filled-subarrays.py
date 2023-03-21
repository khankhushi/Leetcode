class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = zeroSubarraysAtCurr = 0
        for num in nums:
            if num == 0:
                zeroSubarraysAtCurr += 1
                cnt += zeroSubarraysAtCurr
            else:
                zeroSubarraysAtCurr = 0
        return cnt
        