class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        outerarr = []
        while nums:
            unique_elements = set(nums)
            innerarr = []
            for i in unique_elements:
                innerarr.append(i)
                nums.remove(i)
            outerarr.append(innerarr)
        return outerarr
        