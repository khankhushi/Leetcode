class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]== target and i!=j:
                    res.append(i)
                    res.append(j)
                else:
                    continue
        return res
        