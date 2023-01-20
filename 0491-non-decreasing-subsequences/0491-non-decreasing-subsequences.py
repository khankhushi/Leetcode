class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(index, temp):
            if index == len(nums):
                if len(temp) >= 2:
                    res.add(tuple(temp[:]))
                return
            if (temp==[] or temp[-1] <= nums[index]):
                dfs(index +1, temp + [nums[index]])

            dfs(index+1, temp)

        dfs(0, [])

        return res