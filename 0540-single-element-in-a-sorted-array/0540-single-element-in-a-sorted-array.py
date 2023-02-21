class Solution:
    def singleNonDuplicate(self, nums):
        mp = Counter(nums)
        for c, freq in mp.items():
            if freq == 1: 
                return c